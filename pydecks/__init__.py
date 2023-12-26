import os
import json
from enum import Enum
from typing import Dict, Type, Optional, Union, List

import requests

from .models import _BaseModel, model_classes, model_cache
from .models import *
from .utils import unpascalize


BASE_URL = "https://api.codecks.io"


class Operator(Enum):
    EQ = ("eq", "value | null")
    NEQ = ("neq", "value | null")
    IN = ("in", "array")
    NOT_IN = ("notIn", "array")
    GT = ("gt", "ordinal value")
    GTE = ("gte", "ordinal value")
    LT = ("lt", "ordinal value")
    LTE = ("lte", "ordinal value")
    IN_OR_NULL = ("inOrNull", "array")
    CONTAINS = ("contains", "string (if field is of type string)")
    HAS = ("has", "value (if field is of type array)")
    OVERLAPS = ("overlaps", "array (if field is of type array)")
    SEARCH = (
        "search",
        "string if field is searchable (so far only available for the content field within the card model)",
    )

    def __init__(self, operator, description):
        self.operator = operator
        self.description = description

    def __str__(self):
        return self.operator

    def __repr__(self):
        return self.operator


class Query:
    def __init__(
        self,
        relname: Type[_BaseModel],
        filter: Optional[Dict[str, Union[str, int, dict, list]]] = None,
        fields: Optional[List[_BaseModel.Fields]] = None,
        relations: Optional[Dict[_BaseModel.Relations, "Query"]] = None,
    ):
        self._relname = unpascalize(relname.__name__)
        self._filter = filter or {}
        self._fields = [field.value for field in fields] if fields else []
        self._relations = relations or {}

    @property
    def filter_json(self):
        return json.dumps(self._filter) if self._filter else ""

    @property
    def relations(self):
        relations = []
        for rel in self._relations:
            key = (
                f"{rel}({self._relations[rel].filter_json})"
                if self._relations[rel]._filter
                else f"{rel}"
            )
            value = self._relations[rel]._fields + self._relations[rel].relations
            relations.append({key: value})
        return relations

    @property
    def all_fields(self):
        return self._fields + self.relations

    def __repr__(self):
        return f"{self._relname}({self.filter_json}): {self.all_fields}"

    def __dict__(self):
        return {self._relname: self.all_fields}

    def __iter__(self):
        yield self._relname, self.all_fields

    def json(self):
        return json.dumps(self.__dict__())


class Codecks:
    def __init__(self, subdomain, api_token=None):
        self._token = api_token or os.environ.get("CODECKS_TOKEN", "")
        if not self._token:
            raise ValueError("No token provided")
        self._base_headers = {
            "X-Account": subdomain,
            "X-Auth-Token": self._token,
        }

    def run_query(self, query: Union[Query, dict]):
        if isinstance(query, dict):
            data = query
        elif query._relname == "_root":
            data = {"query": dict(query)}
        elif query._relname == "account":
            data = {"query": {"_root": dict(query)}}
        elif self.is_in_account(query):
            data = {
                "query": {
                    "_root": [
                        dict(Query(Account, relations={f"{query._relname}s": query}))
                    ]
                }
            }
        else:
            raise ValueError("Query not valid")

        return self.parse_response(self._send_request(data))

    def _send_request(self, data: dict):
        headers = self._base_headers
        headers["Content-Type"] = "application/json"
        res = requests.post(
            url=BASE_URL,
            headers=headers,
            data=json.dumps(data),
        )
        return res.json()

    def is_in_account(self, query: Query) -> bool:
        return any(
            (f"{query._relname}s" == member.value for member in Account.Relations)
        )

    def parse_response(self, data: dict) -> Dict[str, _BaseModel]:
        results = {}
        for model_name, model_datas in data.items():
            results[model_name] = {}
            if model_name == "_root":
                results[model_name] = model_cache.get(model_name, "_root", model_datas)
            else:
                for id, item_data in model_datas.items():
                    results[model_name][id] = model_cache.get(model_name, id, item_data)
        return results

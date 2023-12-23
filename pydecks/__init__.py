import os
import json
from enum import Enum
from typing import Dict

import requests

from . import models
from .models_list import *

model_cache = models.model_cache


def parse_response(data: dict) -> Dict[str, models._BaseModel]:
    results = {}
    for model_name, model_datas in data.items():
        results[model_name] = {}
        if model_name == "_root":
            results[model_name] = model_cache.get(model_name, "_root", model_datas)
        else:
            for id, item_data in model_datas.items():
                results[model_name][id] = model_cache.get(model_name, id, item_data)
    return results


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
    def __init__(self):
        self._query = {"_root": []}


class Codedeck:
    def __init__(self, subdomain, api_token=None):
        self._token = api_token or os.environ.get("CODECKS_TOKEN", "")
        if not self._token:
            raise ValueError("No token provided")
        self._base_headers = {
            "X-Account": subdomain,
            "X-Auth-Token": self._token,
        }

    def get(self, query, fields):
        headers = self._base_headers
        headers["Content-Type"] = "application/json"
        res = requests.post(
            url=BASE_URL,
            headers=headers,
            data=json.dumps({"query": {"_root": [{"account": [{query: fields}]}]}}),
        )
        return res.json()

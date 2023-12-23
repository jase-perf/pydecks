import os
import base64
import json
from enum import Enum
from typing import Dict

import requests

from . import models

model_cache = models.model_cache


def parse_response(data: dict) -> Dict[str, models._BaseModel]:
    results = {}
    for model_name, model_datas in data.items():
        results[model_name] = {}
        for id, data in model_datas.items():
            results[model_name][id] = model_cache.get(model_name, id, data)


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
    def __init__(self, model):
        self.model = model
        self.query = {}
        self.special_fields = {}

    def filter(self, field, value, operator="eq"):
        if field.startswith("!"):
            field = field[1:]
            negation = True
        else:
            negation = False

        if isinstance(value, dict) or operator != "eq":
            filter_value = {"op": operator, "value": value}
        else:
            filter_value = value

        self.query[field] = filter_value
        if negation:
            self.query = {f"!{field}": self.query[field]}

        return self

    def or_(self, *args):
        self.special_fields["$or"] = args
        return self

    def and_(self, *args):
        self.special_fields["$and"] = args
        return self

    def order(self, field, direction="asc"):
        self.special_fields["$order"] = {"field": field, "dir": direction}
        return self

    def limit(self, limit):
        self.special_fields["$limit"] = limit
        return self

    def offset(self, offset):
        self.special_fields["$offset"] = offset
        return self

    def first(self, first=True):
        self.special_fields["$first"] = first
        return self

    def build(self):
        final_query = {**self.query, **self.special_fields}
        return f"{self.model}({json.dumps(final_query)})"


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


# res = requests.post(
#     url=BASE_URL,
#     headers={
#         "X-Account": "argonautcreations",
#         "X-Auth-Token": os.environ.get("CODECKS_TOKEN", ""),
#         "Content-Type": "application/json",
#     },
#     json=
# )

# Example usage
query = Query("card").filter("title", "API", operator="contains")
print(query.build())
cd = Codedeck("argonautcreations")
result = cd.get(query=query.build(), fields=["id", "title"])
print(result)

"""markdown
The Codecks API is heavily inspired by GraphQL. When Codecks was started, only the idea of GraphQL has been around, but no implementation. So Codecks developed its own JSON-based querying language.

This reference only covers read operations. Please refer to the Quick Guide to Codecks API for information about write operations.

Basics
simple syntax example:

{
  "_root": [{
    "relname($query)": [...fields and relations],
    "relname($query2)": [...fields and relations],
  }]
}
curl example:

curl 'https://api.codecks.io/' \
  -H 'X-Account: [SUBDOMAIN]' \
  -H 'Content-Type: application/json' \
  -H 'X-Auth-Token: [TOKEN]' \
  --data-binary '{"query":{"_root":[{"account":["name"]}]}}'
The Token corresponds to the value of the at cookie sent to api.codecks.io requests. A feature for dedicated API-Tokens is planned.

relname($query)
here’s the syntax for what a $query looks like.

{fieldName1: $val, fieldName2: {"op": $op, "value": $val}}
Note that {fieldName1: $val} is a shortcut for {fieldName1: {"op": "eq", "value": $val}}

The $query portion needs to be sent to JSON.stringify() or similar. For readiablity’s sake we display the non-stringified versions here.

If you want to fetch all related items you can leave out the $query portion like this:

...
"deck": [{
  "cards": [...fields and relations],
}]
...
Possible values for $op
eq: value | null
neq: value | null
in: array
notIn: array
gt: ordinal value
gte: ordinal value
lt: ordinal value
lte: ordinal value
inOrNull: array
contains: string (if field is of type string)
has: value (if field is of type array)
overlaps: array (if field is of type array)
search: string if field is searchable (so far only available for the content field within the card model)
Filtering by values of relation fields
fieldName can also be used to access a relation’s properties. For a card this could be e.g {resolvables: {context: ["block", "review"], isClosed: false}}. This would fetch all cards that have at least one non-closed resolvable with the blockorreview context

Negation:

you can also do {!resolvables: {context: ["block", "review"], isClosed: false}} to say only show cards with no such resolvables.

“in” - shortcut
relname({"projectId": [123, 234]})
is equivalent to

relname({"projectId": {"op": "in", value: [123, 234]}})
special fields
$or combines multiple queries via or, sub queries may not contain special fields (beside more $or and $and)

relname({"$or": [{"isArchived": true}, {"status": "done"}]})
$and combines multiple queries via and, sub queries may not contain special fields (beside more $or and $and)

relname({"$and": [
  {"effort": {"op": "gt", value: 0}},
  {"effort": {"op": "lte", value: 5}}
]})
$order: OrderExpression

relname({"deckId": 123, "$order": "createdAt"})
Full OrderExpression is {"field": fieldName, "dir": "desc"|"asc"}[]

Shortcuts are

{"field": fieldName, "dir": "desc"|"asc"} -> [{"field": fieldName, "dir": "desc"|"asc"}]
fieldName -> [{"field": fieldName, "dir": "asc"}]
-fieldName -> [{"field": fieldName, "dir": "desc"}]
$first: true

only works when order is provided, return singleton

relname({"deckId": 123, "$order": "createdAt", "$first": true})
$limit: number

only works when order is provided, there’s always a maximum $limit of 3000

relname({"deckId": 123, "$order": "createdAt", "$limit": 10})
$offset: number

only works when limit (and thus order) is provided

relname({"deckId": 123, "$order": "createdAt", "$limit": 10, "$offset": 20})
root level id-based queries
root level queries look like this:

{
  "modelname($id)": [...fields and relations]
}
$id is either a string for single id models or a JSON array for compound ids.


"""

import pydecks
import json


card = pydecks.model_cache.get_id("806284a6-9ee0-11ee-b457-23a5fa5d2532")
print(repr(card))

print("----")

print(pydecks.Card.__name__)

query = pydecks.Query(
    pydecks.Card,
    filter={"title": {"op": "contains", "value": "Python"}},
    fields=[pydecks.Card.Fields.content, pydecks.Card.Fields.title],
    relations={
        pydecks.Card.Relations.cardReferences: pydecks.Query(
            pydecks.Card,
            fields=[pydecks.Card.Fields.title, pydecks.Card.Fields.content],
        )
    },
)
# print(query.relations)
print(query)
print(query.json())


print(f"Enum value: {pydecks.Card.Fields.content}")
print(f"Operator: {pydecks.Operator.EQ}")

print("----")

nested = pydecks.Query(
    pydecks.Root,
    relations={
        pydecks.Root.Relations.account: pydecks.Query(
            pydecks.Account,
            relations={
                pydecks.Account.Relations.cards: pydecks.Query(
                    pydecks.Card,
                    filter={"title": {"op": "contains", "value": "Python"}},
                    fields=[pydecks.Card.Fields.content, pydecks.Card.Fields.title],
                    relations={
                        pydecks.Card.Relations.cardReferences: pydecks.Query(
                            pydecks.Card,
                            fields=[
                                pydecks.Card.Fields.title,
                                pydecks.Card.Fields.content,
                            ],
                        )
                    },
                )
            },
        )
    },
)

print(nested)

print(json.dumps(dict(nested)))

print("----")

cd = pydecks.Codecks("argonautcreations")

card_query = pydecks.Query(
    pydecks.Card,
    filter={"title": {"op": "contains", "value": "Python"}},
    fields=[pydecks.Card.Fields.content, pydecks.Card.Fields.title],
    relations={
        pydecks.Card.Relations.cardReferences: pydecks.Query(
            pydecks.Card,
            fields=[
                pydecks.Card.Fields.title,
                pydecks.Card.Fields.content,
            ],
        )
    },
)

response = cd.run_query(card_query)

print(response)

print("----")

from pydecks import Query, Card, Codecks, Attachment, File

q = Query(
    Card,
    filter={"content": {"op": "contains", "value": "wepon"}},
    fields=[Card.Fields.content, Card.Fields.assignee, Card.Fields.isDoc],
    relations={
        Card.Relations.attachments: Query(
            Attachment,
            relations={
                Attachment.Fields.file: Query(
                    File, fields=[File.Fields.size, File.Fields.name]
                )
            },
        )
    },
)

codecks = Codecks(
    "argonautcreations",
)

result = codecks.run_query(q)

print(result)

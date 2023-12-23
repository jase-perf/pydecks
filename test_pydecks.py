import pydecks

test_response = {
    "account": {
        "836c6d90-9ed8-11ee-b457-575f7d800983": {
            "id": "836c6d90-9ed8-11ee-b457-575f7d800983",
            'cards({"$order": "-createdAt"})': [
                "1817b79e-9eeb-11ee-b457-f7be2ff8d2c3",
                "806284a6-9ee0-11ee-b457-23a5fa5d2532",
                "5f9a7405-9ee0-11ee-b457-47cea7c73d30",
                "5c1290b5-9ee0-11ee-b457-6bf2647e5c2d",
                "61d1dca4-9edf-11ee-b457-0f45f3406428",
                "b6006878-9ed9-11ee-b457-9fe001fe6636",
                "54704650-9ed9-11ee-b457-fbae4f3dbcaf",
                "233f9131-9ed9-11ee-b457-5759e1c8cf4a",
            ],
        }
    },
    "_root": {"account": "836c6d90-9ed8-11ee-b457-575f7d800983"},
    "card": {
        "1817b79e-9eeb-11ee-b457-f7be2ff8d2c3": {
            "title": "Testing an image from python!",
            "creator": "802b62e4-9ed8-11ee-b457-ef6fbeedd831",
            "createdAt": "2023-12-20T03:51:45.360Z",
            "cardId": "1817b79e-9eeb-11ee-b457-f7be2ff8d2c3",
            "accountId": "836c6d90-9ed8-11ee-b457-575f7d800983",
        },
        "806284a6-9ee0-11ee-b457-23a5fa5d2532": {
            "title": "Add Wepons!",
            "creator": "802b62e4-9ed8-11ee-b457-ef6fbeedd831",
            "createdAt": "2023-12-20T02:35:55.866Z",
            "cardId": "806284a6-9ee0-11ee-b457-23a5fa5d2532",
            "accountId": "836c6d90-9ed8-11ee-b457-575f7d800983",
        },
        "5f9a7405-9ee0-11ee-b457-47cea7c73d30": {
            "title": "Wepon #2",
            "creator": "802b62e4-9ed8-11ee-b457-ef6fbeedd831",
            "createdAt": "2023-12-20T02:35:00.861Z",
            "cardId": "5f9a7405-9ee0-11ee-b457-47cea7c73d30",
            "accountId": "836c6d90-9ed8-11ee-b457-575f7d800983",
        },
        "5c1290b5-9ee0-11ee-b457-6bf2647e5c2d": {
            "title": "Wepon #1",
            "creator": "802b62e4-9ed8-11ee-b457-ef6fbeedd831",
            "createdAt": "2023-12-20T02:34:54.922Z",
            "cardId": "5c1290b5-9ee0-11ee-b457-6bf2647e5c2d",
            "accountId": "836c6d90-9ed8-11ee-b457-575f7d800983",
        },
        "61d1dca4-9edf-11ee-b457-0f45f3406428": {
            "title": "Show Deedee",
            "creator": "802b62e4-9ed8-11ee-b457-ef6fbeedd831",
            "createdAt": "2023-12-20T02:27:55.097Z",
            "cardId": "61d1dca4-9edf-11ee-b457-0f45f3406428",
            "accountId": "836c6d90-9ed8-11ee-b457-575f7d800983",
        },
        "b6006878-9ed9-11ee-b457-9fe001fe6636": {
            "title": "Test task",
            "creator": "802b62e4-9ed8-11ee-b457-ef6fbeedd831",
            "createdAt": "2023-12-20T01:47:19.344Z",
            "cardId": "b6006878-9ed9-11ee-b457-9fe001fe6636",
            "accountId": "836c6d90-9ed8-11ee-b457-575f7d800983",
        },
        "54704650-9ed9-11ee-b457-fbae4f3dbcaf": {
            "title": "API Docs",
            "creator": "802b62e4-9ed8-11ee-b457-ef6fbeedd831",
            "createdAt": "2023-12-20T01:44:35.657Z",
            "cardId": "54704650-9ed9-11ee-b457-fbae4f3dbcaf",
            "accountId": "836c6d90-9ed8-11ee-b457-575f7d800983",
        },
        "233f9131-9ed9-11ee-b457-5759e1c8cf4a": {
            "title": "Check the codecks API docs.",
            "creator": "802b62e4-9ed8-11ee-b457-ef6fbeedd831",
            "createdAt": "2023-12-20T01:43:14.601Z",
            "cardId": "233f9131-9ed9-11ee-b457-5759e1c8cf4a",
            "accountId": "836c6d90-9ed8-11ee-b457-575f7d800983",
        },
    },
}


results = pydecks.parse_response(test_response)
print(results)

print("----")

card = pydecks.model_cache.get_id("806284a6-9ee0-11ee-b457-23a5fa5d2532")
print(repr(card))

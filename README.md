# pydecks
Python library for the Codecks API

NOTE: This is very much a work in progress! It will likely change significantly as it is developed. Please use it and give feedback or submit pull requests if you want to contribute. This is my first time creating a library like this, so I'm sure there are many things that could be improved.

The goal of this library is to provide a pythonic interface to the GraphQL-esque API of [Codecks](https://codecks.io/), as explained in the [API documentation](https://manual.codecks.io/api-reference/).

The full API schema is not yet available from Codecks, so the library was created by parsing the API documentation (this is what `pydecks/update_models.py` does). This means that the library may not be up to date with the latest API version and may not be accurate if the documentation is not. If you run into issues, please open an issue on the github repository or submit a pull request to help out.

## Features
One of the main goals is to take advantage of modern Python features such as type hints to make the library easy to use via and IDE so that autocompletion, type checking, and docstrings are available for more information.

For example, when requesting a card, you will create a query using the Card class, which will provide autocompletion for the fields available in the API. The available fields are available in an Enum in the class, so you can use that to know which fields are available for each object type. When you hover over the field, you will see a docstring in your IDE that includes the type of the field.

This is particularly helpful for References, which in turn include their own nested fields. By checking the docstring for a reference, you can see which object Type it will return and then use that class to know which fields are available for that object type.


## Todo

- [ ] Filters for queries currently require a normal dictionary to be passed in, like you would with a plain JSON query. It would be nice to have a more pythonic way to do this, such as using a class or multiple classes for different filters like "eq", "in", etc.
- [ ] Create some convenience methods for common queries or actions. The main one that comes to mind is to upload an attachment to a card and set it as the card's image. (There is some starter code for this already.)
- [ ] Add more official tests with pytest or another testing framework. Currently, the only tests are manual ones in the `test_pydecks.py` file.
- [ ] Add more documentation and examples.
- [ ] Find way to simplify the interface.
- [ ] Get access to the real JSON schema and use that to generate the models instead of parsing the API documentation.
- [ ] Make the response into an object that has properties for all of the different types, which could help with intellisense for the exptected types of the response.

## Example Usage

Get all cards that contain the word "wepon" in the content (which includes the title by default) and get any attachments on those cards with their filenames and sizes.

```python
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

codecks = Codecks(subdomain = "mysubdomain") # API Token can be set with env variable CODECKS_TOKEN or passed in as an argument. 

result = codecks.run_query(q)
```

This will return a response in the same format as the API would normally return, except that all ID links will be replaced with the actual objects. For example, the assignee field will be a User object instead of a string ID. 

In the above example, the response will be a list of Card objects, each of which will have a list of Attachment objects, each of which will have a File object. All of those objects are linked to each other, so you can access the file object directly from the card like this:
For example, to get the filename of the first attachment on the first card, you can do this:

`result["card"][0].attachments[0].file.name`


Additionally, instead of returns a dict of dicts for each object returned, the response will be a dict of lists, which will make it easier to iterate through them.


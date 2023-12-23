import datetime
import sys
import inspect
import re
from dateutil.parser import parse
from weakref import WeakValueDictionary

from .utils import is_valid_uuid, pascalize


class _ModelCache:
    _instance = None
    __model_cache = WeakValueDictionary()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(_ModelCache, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def get(cls, model_name, id, data=None):
        if id in cls.__model_cache:
            if data:
                cls.__model_cache[id].update(data)
            return cls.__model_cache[id]
        else:
            model_name = pascalize(model_name)
            model_class = model_classes.get(model_name)
            if not model_class:
                raise ValueError(f"No model found for {model_name}")
            model = model_class(id, data)
            cls.__model_cache[id] = model
            return model

    @classmethod
    def exists(cls, id):
        return id in cls.__model_cache

    @classmethod
    def get_id(cls, id, default=None):
        return cls.__model_cache.get(id, default)

    def __len__(self):
        return len(self.__model_cache)

    def __iter__(self):
        return iter(self.__model_cache.values())

    def __str__(self):
        return f"<ModelCache: {len(self.__model_cache)} items>"

    def __repr__(self):
        return str(self)

    def __contains__(self, item):
        return item in self.__model_cache


class _BaseModel:
    def __init__(self, id, data=None):
        self.id = id
        if data:
            self.update(data)

    def update(self, data):
        for key, value in data.items():
            if key == "id":
                setattr(self, key, value)
            elif is_valid_uuid(value):
                setattr(self, key, model_cache.get(value))
            elif isinstance(value, list):
                for item in value:
                    if is_valid_uuid(item):
                        setattr(self, key, model_cache.get(item))
                    elif isinstance(item, str):
                        setattr(self, key, optional_datetime(item))
                    else:
                        setattr(self, key, item)
            elif isinstance(value, str):
                setattr(self, key, optional_datetime(value))
            else:
                setattr(self, key, value)

    def properties(self):
        return [
            prop
            for prop in dir(self)
            if not prop.startswith("_") and not callable(getattr(self, prop))
        ]

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.id}>"

    def __repr__(self):
        return f"""{self.__class__.__name__}: {self.id} {{
    {''',
'''.join([f"    {prop}: {getattr(self, prop)}" for prop in self.properties()])}
}}"""


def optional_datetime(string, fuzzy=False):
    if not re.match(r"\d{4}-\d{2}-\d{2}", string):
        return string
    try:
        return parse(string, fuzzy=fuzzy)
    except ValueError:
        return string


class Unknown(_BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


from .models_list import *

# For convenience, create list of all the model classes:
model_classes = {
    model[0]: model[1]
    for model in inspect.getmembers(sys.modules[__name__], inspect.isclass)
    if model[1] not in [_BaseModel, Unknown]
}

# Create a single instance of the model cache for convenience:
model_cache = _ModelCache()

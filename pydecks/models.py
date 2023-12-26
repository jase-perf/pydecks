from typing import Optional, get_type_hints
import sys
import inspect
import re
from dateutil.parser import parse
from weakref import WeakValueDictionary
from abc import ABC
from enum import Enum

from .utils import is_valid_uuid, pascalize


class _ModelCache:
    _instance = None
    __model_cache = WeakValueDictionary()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(_ModelCache, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def get(cls, model_name: str, id: str, data: Optional[dict] = None):
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
    def exists(cls, id: str):
        return id in cls.__model_cache

    @classmethod
    def get_id(cls, id: str, default=None):
        return cls.__model_cache.get(id, default)

    def __len__(self):
        return len(self.__model_cache)

    def __iter__(self):
        return iter(self.__model_cache.values())

    def __str__(self):
        return f"<ModelCache: {len(self.__model_cache)} items>"

    def __repr__(self):
        return str(self)

    def __contains__(self, id: str) -> bool:
        return id in self.__model_cache


class _BaseModel(ABC):
    class Fields(Enum):
        pass

    class Relations(Enum):
        pass

    def __init__(self, id: str, data: Optional[dict] = None):
        self.id = id
        if data:
            self.update(data)

    def update(self, data: dict):
        for key, value in data.items():
            key = key.split("(")[0]
            if key == "id":
                setattr(self, key, value)
            elif key.lower().endswith("id"):
                if key[:-2] == self.__class__.__name__.lower():
                    setattr(self, "id", value)
                elif is_valid_uuid(value):
                    model_name = get_classname_from_hint(self.__class__, key[:-2])
                    setattr(self, key[:-2], model_cache.get(model_name, value))
            elif isinstance(value, list):
                for item in value:
                    if is_valid_uuid(item):
                        model_name = get_classname_from_hint(self.__class__, key)
                        setattr(self, key, model_cache.get(model_name, item))
                    elif isinstance(item, str):
                        setattr(self, key, optional_datetime(item))
                    else:
                        setattr(self, key, item)
            elif is_valid_uuid(value):
                model_name = get_classname_from_hint(self.__class__, key)
                setattr(self, key, model_cache.get(model_name, value))
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


def get_classname_from_hint(cls, key):
    type_hint = get_type_hints(cls).get(key, "Unknown")
    if hasattr(type_hint, "__origin__") and issubclass(type_hint.__origin__, list):
        type_hint = type_hint.__args__[0]
    return type_hint.__name__


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

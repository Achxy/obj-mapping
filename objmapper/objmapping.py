"""

"""
from __future__ import annotations

from types import MappingProxyType
from typing import Annotated, Any

from _abstracted import AbstractAnnotationContainer
from metaobjmapping import MetaObjectMapping

from .enums import IMMUTABLE, MUTABLE, Mutability


class ObjectMapping(AbstractAnnotationContainer, metaclass=MetaObjectMapping):
    __blueprint__: type[ObjectMapping] | None = None
    __final__: bool = False
    __default_mutability__: Mutability = IMMUTABLE

    def __init_subclass__(
        cls: type[ObjectMapping],
        final: bool = True,
        default_mutability: Mutability = IMMUTABLE,
    ) -> None:
        if cls.__final__:
            raise TypeError("Cannot subclass finalized object mapping class")
        cls.__final__ = final

    def __init__(self, mapping: dict) -> None:
        for key, value in mapping.items():
            print(key, value)

    def _assign(self, key, value):
        if key not in self:
            raise KeyError(f"{key!r} not defined in annotations")


class Foo(ObjectMapping, final=True):
    f: int


class Bar(Foo):
    x: str


Foo({})
Bar({})

from types import MappingProxyType
from typing import Any

from _typeshack import AnnotationDict, ProxyAnnotationDict

from objmapper.enums import Mutability


class AnnotationConstructionBlueprint:
    def __init__(self, annotations: AnnotationDict, *, default_mutability: Mutability) -> None:
        self._store: AnnotationDict = {}
        self._annotations: AnnotationDict = annotations
        self._default_mutability = default_mutability

    def assign(self, key, value):
        if key not in self._annotations:
            raise KeyError()
        target = ...

    @property
    def contents(self) -> ProxyAnnotationDict:
        return MappingProxyType(self._store)

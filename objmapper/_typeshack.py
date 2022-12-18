from enum import Enum, auto
from types import MappingProxyType
from typing import Any, Literal, TypeAlias, TypeVar

T = TypeVar("T")

AnnotationDict: TypeAlias = dict[str, Any]
ProxyAnnotationDict: TypeAlias = MappingProxyType[str, Any]

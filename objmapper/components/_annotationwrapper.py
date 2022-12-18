from typing import Any

from objmapper.enums import Mutability


class AnnotationWrapper:
    def __init__(self, annotation: Any, default_mutability: Mutability) -> None:
        self.annotation = annotation
        self.default_mutability = default_mutability

    @property
    def is_mutable(self):
        ...

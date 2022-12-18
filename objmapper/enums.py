from enum import Enum, auto


class Mutability(Enum):
    MUTABLE = auto()
    IMMUTABLE = auto()


MUTABLE = Mutability.MUTABLE
IMMUTABLE = Mutability.IMMUTABLE

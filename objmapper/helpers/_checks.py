from typing import Any

from _typeshack import T


def check_and_return(
    obj: T,
    expected: type[T],
    exc: type[BaseException] = TypeError,
    template: str = "Expected object `{obj}` to be of type {expected} got {got} instead",
) -> T:
    if not isinstance(obj, expected):
        msg = template.format(obj=repr(obj), expected=expected, got=type(obj))
        raise exc(msg)
    return obj

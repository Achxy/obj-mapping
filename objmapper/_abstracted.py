class AbstractAnnotationContainer:
    __slots__ = ()

    def __contains__(self, item: str) -> bool:
        return item in self.__annotations__

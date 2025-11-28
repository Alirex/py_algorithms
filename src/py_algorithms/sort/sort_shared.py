from typing import Any, Protocol

from pydantic import BaseModel


class Comparable[T](Protocol):  # noqa: PLW1641
    def __lt__(self, value: T, /) -> bool: ...

    def __gt__(self, value: T, /) -> bool: ...

    def __le__(self, value: T, /) -> bool: ...
    def __ge__(self, value: T, /) -> bool: ...

    def __eq__(self, value: object, /) -> bool: ...
    def __ne__(self, value: object, /) -> bool: ...


class Some(BaseModel):  # noqa: PLW1641
    value: int

    def __lt__(self, value: Any) -> bool:  # noqa: ANN401
        return self.value < value.value if isinstance(value, Some) else NotImplemented

    #
    def __gt__(self, value: Any) -> bool:  # noqa: ANN401
        return self.value > value.value if isinstance(value, Some) else NotImplemented

    def __le__(self, value: Any) -> bool:  # noqa: ANN401
        return self.value <= value.value if isinstance(value, Some) else NotImplemented

    def __ge__(self, value: Any) -> bool:  # noqa: ANN401
        return self.value >= value.value if isinstance(value, Some) else NotImplemented

    def __eq__(self, value: object) -> bool:
        return self.value == value.value if isinstance(value, Some) else NotImplemented

    def __ne__(self, value: object) -> bool:
        return self.value != value.value if isinstance(value, Some) else NotImplemented

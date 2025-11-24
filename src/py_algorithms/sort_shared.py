from typing import Any, Protocol

from pydantic import BaseModel


class Sortable(Protocol):
    def __lt__(self, other: Any) -> bool: ...  # noqa: ANN401

    def __gt__(self, other: Any) -> bool: ...  # noqa: ANN401

    def __le__(self, other: Any) -> bool: ...  # noqa: ANN401
    def __ge__(self, other: Any) -> bool: ...  # noqa: ANN401


class Some(BaseModel):
    value: int

    def __lt__(self, other: Any) -> bool:  # noqa: ANN401
        return self.value < other.value if isinstance(other, Some) else NotImplemented

    #
    def __gt__(self, other: Any) -> bool:  # noqa: ANN401
        return self.value > other.value if isinstance(other, Some) else NotImplemented

    def __le__(self, other: Any) -> bool:  # noqa: ANN401
        return self.value <= other.value if isinstance(other, Some) else NotImplemented

    def __ge__(self, other: Any) -> bool:  # noqa: ANN401
        return self.value >= other.value if isinstance(other, Some) else NotImplemented

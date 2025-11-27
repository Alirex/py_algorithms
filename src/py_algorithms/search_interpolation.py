from typing import TYPE_CHECKING, Any, Protocol

from py_algorithms.sort_shared import Comparable

if TYPE_CHECKING:
    from collections.abc import Sequence

    from py_algorithms.search_shared import PositionOrMinusOne


class ComparableWithSubtraction[T](Comparable[T], Protocol):
    def __sub__(self: T, value: T, /) -> T: ...


def interpolation_search[T: ComparableWithSubtraction[Any]](arr: Sequence[T], x: T) -> PositionOrMinusOne:
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        index = low + int((float(high - low) / (arr[high] - arr[low])) * (x - arr[low]))
        if arr[index] == x:
            return index
        if arr[index] < x:
            low = index + 1
        else:
            high = index - 1

    return -1


def main() -> None:
    arr = [1, 3, 5, 7, 9, 11, 14, 16, 18, 20, 22, 25, 28, 30]
    index = interpolation_search(arr, 25)  # 11
    print(arr[index])  # 25


if __name__ == "__main__":
    main()

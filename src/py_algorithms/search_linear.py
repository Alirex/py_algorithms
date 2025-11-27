from typing import TYPE_CHECKING, Any

from py_algorithms.sort_shared import Comparable

if TYPE_CHECKING:
    from collections.abc import Sequence

    from py_algorithms.search_shared import PositionOrMinusOne


def linear_search[T: Comparable[Any]](arr: Sequence[T], x: T) -> PositionOrMinusOne:
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def exists_in_list[T: Comparable[Any]](arr: list[T], x: T) -> bool:
    # return linear_search(arr, x) != -1
    return bool(~linear_search(arr, x))


def main() -> None:
    numbers = [1, 3, 5, 7, 9, 11]
    print(linear_search(numbers, 7))  # Output: 3

    print(exists_in_list(numbers, 7))  # Output: True
    print(exists_in_list(numbers, 2))  # Output: False


if __name__ == "__main__":
    main()

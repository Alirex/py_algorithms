from typing import TYPE_CHECKING, Any

from py_algorithms.sort_shared import Comparable, Some

if TYPE_CHECKING:
    from collections.abc import MutableSequence


def bubble_sort[T: Comparable[Any]](arr: MutableSequence[T]) -> None:
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main() -> None:
    numbers = [5, 3, 8, 4, 2]

    bubble_sort(numbers)

    # noinspection Assert
    assert numbers == [2, 3, 4, 5, 8]  # noqa: S101
    print(numbers)

    numbers_2 = [Some(value=5), Some(value=3), Some(value=8), Some(value=4), Some(value=2)]
    bubble_sort(numbers_2)

    print(numbers_2)


if __name__ == "__main__":
    main()

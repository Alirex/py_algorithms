from typing import TYPE_CHECKING

from py_algorithms.sort_shared import Some, Sortable

if TYPE_CHECKING:
    from collections.abc import MutableSequence


def selection_sort[T: Sortable](arr: MutableSequence[T]) -> None:
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main() -> None:
    numbers = [5, 3, 8, 4, 2]

    selection_sort(numbers)  # pyright: ignore[reportArgumentType]

    # noinspection Assert
    assert numbers == [2, 3, 4, 5, 8]  # noqa: S101
    print(numbers)

    numbers_2 = [Some(value=5), Some(value=3), Some(value=8), Some(value=4), Some(value=2)]
    selection_sort(numbers_2)

    print(numbers_2)


if __name__ == "__main__":
    main()

from typing import TYPE_CHECKING

from py_algorithms.sort_shared import Some, Sortable

if TYPE_CHECKING:
    from collections.abc import MutableSequence


def bubble_sort[T: Sortable](lst: MutableSequence[T]) -> None:
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def main() -> None:
    numbers = [5, 3, 8, 4, 2]

    bubble_sort(numbers)  # pyright: ignore[reportArgumentType]

    # noinspection Assert
    assert numbers == [2, 3, 4, 5, 8]  # noqa: S101
    print(numbers)

    numbers_2 = [Some(value=5), Some(value=3), Some(value=8), Some(value=4), Some(value=2)]
    bubble_sort(numbers_2)

    print(numbers_2)


if __name__ == "__main__":
    main()

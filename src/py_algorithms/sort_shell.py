from typing import TYPE_CHECKING, Any

from py_algorithms.sort_shared import Comparable, Some

if TYPE_CHECKING:
    from collections.abc import MutableSequence


def shell_sort[T: Comparable[Any]](arr: MutableSequence[T]) -> MutableSequence[T]:
    n: int = len(arr)
    gap: int = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


def main() -> None:
    numbers = [5, 3, 8, 4, 2]

    shell_sort(numbers)

    # noinspection Assert
    assert numbers == [2, 3, 4, 5, 8]  # noqa: S101
    print(numbers)

    numbers_2 = [Some(value=5), Some(value=3), Some(value=8), Some(value=4), Some(value=2)]
    shell_sort(numbers_2)

    print(numbers_2)


if __name__ == "__main__":
    main()

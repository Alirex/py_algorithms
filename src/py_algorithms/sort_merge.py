from typing import Any

from py_algorithms.sort_shared import Comparable, Some


def merge_sort[T: Comparable[Any]](arr: list[T]) -> list[T]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge[T: Comparable[Any]](left: list[T], right: list[T]) -> list[T]:
    merged: list[T] = []
    left_index = 0
    right_index = 0

    # At first, merge the smaller elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are still elements left in the left or right half,
    # add them to the result
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def main() -> None:
    numbers = [5, 3, 8, 4, 2]

    merge_sort(numbers)

    # noinspection Assert
    assert numbers == [2, 3, 4, 5, 8]  # noqa: S101
    print(numbers)

    numbers_2 = [Some(value=5), Some(value=3), Some(value=8), Some(value=4), Some(value=2)]
    merge_sort(numbers_2)

    print(numbers_2)


if __name__ == "__main__":
    main()

from typing import TYPE_CHECKING, Any

from py_algorithms.sort_shared import Comparable

if TYPE_CHECKING:
    from collections.abc import Sequence

    from py_algorithms.search_shared import PositionOrMinusOne


def binary_search[T: Comparable[Any]](arr: Sequence[T], x: T) -> PositionOrMinusOne:
    low = 0
    high = len(arr) - 1
    # mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, than value at mid, ignore the left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, than value at mid, ignore the right half
        elif arr[mid] > x:
            high = mid - 1

        # Else x is present at mid and return its index
        else:
            return mid

    # If the element is not found
    return -1


def main() -> None:
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binary_search(arr, x)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")


if __name__ == "__main__":
    main()

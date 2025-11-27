from typing import TYPE_CHECKING, Any

from py_algorithms.sort_shared import Comparable

if TYPE_CHECKING:
    from py_algorithms.search_shared import PositionOrMinusOne

type Step = int
"""Step for index table creation"""

type PositionInSourceSequence = int
"""Position in the source sequence"""

type IndexPair[T] = tuple[T, PositionInSourceSequence]
"""Pair of (element, position in source sequence)"""

type IndexTable[T] = list[IndexPair[T]]
"""Index table type"""

type SearchRange = tuple[PositionInSourceSequence, PositionInSourceSequence]
"""Search range type"""


def create_index_table[T](array: list[T], step: Step) -> IndexTable[T]:
    """Creates an index table from the underlying sorted array."""
    return [(array[i], i) for i in range(0, len(array), step)]


def indexed_sequential_search[T: Comparable[Any]](
    array: list[T],
    index_table: IndexTable[T],
    target: T,
) -> PositionOrMinusOne:
    """Performs indexed sequential search on a sorted array using the provided index table."""
    # Search in the index table using binary search
    start = 0
    end = len(index_table) - 1
    while start <= end:
        mid = (start + end) // 2
        if index_table[mid][0] == target:
            return index_table[mid][1]
        if index_table[mid][0] < target:
            start = mid + 1
        else:
            end = mid - 1

    # Defining a range for sequential search
    if start == 0:
        search_range: SearchRange = (0, index_table[0][1])
    elif start >= len(index_table):
        search_range = (index_table[-1][1], len(array))
    else:
        search_range = (index_table[start - 1][1], index_table[start][1])

    # Sequential search in a range
    for i in range(search_range[0], search_range[1]):
        if array[i] == target:
            return i

    return -1  # Element not found


def main() -> None:
    # Main sorted array
    main_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

    # Creating an index table with step 4
    index_table = create_index_table(main_array, 4)

    target = 15
    result = indexed_sequential_search(main_array, index_table, target)
    if result != -1:
        print(f"Element {target} found at position {result}")
    else:
        print(f"Element {target} not found")


if __name__ == "__main__":
    main()

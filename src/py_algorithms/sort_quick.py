from py_algorithms.sort_shared import Some, Sortable


def quicksort[T: Sortable](arr: list[T]) -> list[T]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def main() -> None:
    numbers = [5, 3, 8, 4, 2]

    quicksort(numbers)  # pyright: ignore[reportArgumentType]

    # noinspection Assert
    assert numbers == [2, 3, 4, 5, 8]  # noqa: S101
    print(numbers)

    numbers_2 = [Some(value=5), Some(value=3), Some(value=8), Some(value=4), Some(value=2)]
    quicksort(numbers_2)

    print(numbers_2)


if __name__ == "__main__":
    main()

def sort_bucket(arr: list[int]) -> list[int]:
    max_num = max(arr)

    buckets = [0 for _ in range(max_num + 1)]

    result: list[int] = []
    for num in arr:
        buckets[num] += 1

    for i in range(len(buckets)):
        result.extend(i for _ in range(buckets[i]))

    return result


def main() -> None:
    arr = [3, 89, 67, 254, 9, 21, 185, 4, 62]
    result = sort_bucket(arr)
    print("Відсортований масив:", result)  # Відсортований масив: [3, 4, 9, 21, 62, 67, 89, 185, 254]


if __name__ == "__main__":
    main()

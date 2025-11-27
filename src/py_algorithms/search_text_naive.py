from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from py_algorithms.search_shared import PositionOrMinusOne


def naive_search(main_string: str, pattern: str) -> PositionOrMinusOne:
    pattern_len = len(pattern)
    source_len = len(main_string)

    # Iterate through the characters of the main string.
    # This is the starting index of the substring.
    # So, we don't need to go beyond source_len - pattern_len
    for i in range(source_len - pattern_len + 1):
        j = 0

        # Iterate through the characters of a substring
        while j < pattern_len:
            if main_string[i + j] != pattern[j]:
                break
            j += 1

        # If the value of j is equal to the length of the substring, then the substring is found
        if j == pattern_len:
            return i

    return -1


def main() -> None:
    main_string = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    position = naive_search(main_string, pattern)

    if position != -1:
        print(f"Substring found at position {position}")
    else:
        print("Substring not found in main string.")


if __name__ == "__main__":
    main()

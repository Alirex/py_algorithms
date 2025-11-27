from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from py_algorithms.search_shared import PositionOrMinusOne
    from py_algorithms.search_text_shared import TextPattern


type LPSArray = list[int]
"""Longest Prefix Suffix array type"""


def compute_lps(pattern: TextPattern) -> LPSArray:
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(main_string: str, pattern: TextPattern) -> PositionOrMinusOne:
    pattern_len = len(pattern)
    text_len = len(main_string)

    lps = compute_lps(pattern)

    text_index = 0
    pattern_index = 0

    while text_index < text_len:
        if pattern[pattern_index] == main_string[text_index]:
            text_index += 1
            pattern_index += 1
        elif pattern_index != 0:
            pattern_index = lps[pattern_index - 1]
        else:
            text_index += 1

        if pattern_index == pattern_len:
            return text_index - pattern_index

    return -1  # Pattern not found


def main() -> None:
    raw = "Цей алгоритм часто використовується в текстових редакторах та системах пошуку для ефективного знаходження підрядка в тексті."  # noqa: E501

    pattern = "алг"

    print(kmp_search(raw, pattern))


if __name__ == "__main__":
    main()

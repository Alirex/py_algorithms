from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from py_algorithms.search_shared import PositionOrMinusOne
    from py_algorithms.search_text_shared import TextPattern

type CharacterFromPattern = str
"""Character from pattern type"""

type OffsetByCharacter = int
"""Offset by character type"""

type ShiftTable = dict[CharacterFromPattern, OffsetByCharacter]
"""Shift table type for Boyer-Moore algorithm"""


def build_shift_table(pattern: TextPattern) -> ShiftTable:
    """Create a shift table for the Boyer-Moore algorithm."""
    table: ShiftTable = {}
    length = len(pattern)
    # For each character in the substring, we set an offset equal to the length of the substring
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # If the character is not in the table, the offset will be equal to the length of the substring
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text: str, pattern: TextPattern) -> PositionOrMinusOne:
    # Create a shift table for the pattern (substring)
    shift_table = build_shift_table(pattern)
    print(f"Shift Table: {shift_table}")

    i = 0  # Initialize the starting index for the main text

    # We go through the main text, comparing it with the subtext
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # We start from the end of the substring

        # Compare characters from the end of a substring to its beginning
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Moving to the beginning of the substring

        # If the entire substring matches, return its position in the text
        if j < 0:
            return i  # Substring found

        # Shift index i based on the shift table
        # This allows you to "jump" over non-matching parts of the text
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1  # Substring not found


def main() -> None:
    text = "Being a developer is not easy"
    pattern = "developer"

    position = boyer_moore_search(text, pattern)
    if position != -1:
        print(f"Substring found at index {position}")
    else:
        print("Substring not found")


if __name__ == "__main__":
    main()

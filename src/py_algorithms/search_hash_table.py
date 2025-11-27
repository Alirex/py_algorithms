from typing import Self

from pydantic import BaseModel

type HashIndex = int
"""Hash index type"""

type KeyValuePair[Key, Value] = tuple[Key, Value]
"""Key-Value pair type"""

type Cell[Key, Value] = list[KeyValuePair[Key, Value]]
"""Cell type containing list of key-value pairs"""


class HashTable[Key, Value](BaseModel):
    size: int
    table: list[Cell[Key, Value]]

    @classmethod
    def create(cls, size: int) -> Self:
        return cls(size=size, table=[[] for _ in range(size)])

    def hash_function(self, key: Key) -> HashIndex:
        return hash(key) % self.size

    def insert(self, key: Key, value: Value) -> bool:
        key_hash = self.hash_function(key)
        key_value: KeyValuePair[Key, Value] = (key, value)

        if not self.table[key_hash]:
            self.table[key_hash] = [key_value]
            return True

        for index, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:
                self.table[key_hash][index] = key_value
                return True

        self.table[key_hash].append(key_value)

        return True

    def get(self, key: Key) -> Value | None:
        key_hash = self.hash_function(key)
        if self.table[key_hash]:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


def main() -> None:
    # Testing our hash table:
    hash_table = HashTable[str, int].create(size=5)
    hash_table.insert("apple", 10)
    hash_table.insert("orange", 20)
    hash_table.insert("banana", 30)

    print(hash_table.get("apple"))  # Output: 10
    print(hash_table.get("orange"))  # Output: 20
    print(hash_table.get("banana"))  # Output: 30


if __name__ == "__main__":
    main()

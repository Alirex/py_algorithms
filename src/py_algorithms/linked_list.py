from pydantic import BaseModel


class Node[T](BaseModel):
    data: T
    next: Node[T] | None = None


class LinkedList[T](BaseModel):
    head: Node[T] | None = None

    def insert_at_beginning(self, data: T) -> None:
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: T) -> None:
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node[T] | None, data: T) -> None:
        if prev_node is None:
            print("The given previous node cannot be None.")
            return

        new_node = Node(data=data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: T) -> None:
        current = self.head

        # Head node itself holds the key to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted, keep track of the previous node
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next

        # Node with the key not found
        if current is None:
            return

        if previous is None:
            msg = "Previous node is None while current is not None. This should not happen."
            raise NotImplementedError(msg)

        previous.next = current.next
        current = None

    def search_element(self, data: T) -> Node[T] | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insert_before(self, next_node: Node[T] | None, data: T) -> None:
        if next_node is None:
            print("The given next node cannot be None.")
            return

        new_node = Node(data=data)

        if self.head is None:
            print("The list is empty. Cannot insert before the given node.")
            return

        if self.head == next_node:
            new_node.next = self.head
            self.head = new_node
            return

        current: Node[T] | None = self.head
        while current and current.next != next_node:
            current = current.next

        if current is None:
            print("The given next node is not present in the list.")
            return

        new_node.next = next_node
        current.next = new_node


def first_example() -> None:
    linked_list = LinkedList[int]()

    data_for_node_i_10 = 10
    data_for_node_i_15 = 15

    # Insert nodes at the beginning
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_beginning(data_for_node_i_10)
    linked_list.insert_at_beginning(15)

    # Insert nodes at the end
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(25)

    # Print the linked list
    print("Linked List after insertions:")
    linked_list.print_list()

    # Delete a node
    linked_list.delete_node(data_for_node_i_10)

    print(f"\nLinked List after deletion of {data_for_node_i_10}:")
    linked_list.print_list()

    # Search for an element
    print(f"\nSearching for element {data_for_node_i_15}:")
    element = linked_list.search_element(data_for_node_i_15)
    if element:
        print(element.data)


class SecondExampleModel(BaseModel):
    value: str


def second_example() -> None:
    linked_list = LinkedList[SecondExampleModel]()

    # Insert nodes at the beginning
    linked_list.insert_at_beginning(SecondExampleModel(value="Node 1"))
    linked_list.insert_at_beginning(SecondExampleModel(value="Node 2"))

    # Insert nodes at the end
    node_3 = SecondExampleModel(value="Node 3")
    linked_list.insert_at_end(node_3)
    linked_list.insert_at_end(SecondExampleModel(value="Node 4"))

    # Print the linked list
    print("Linked List of SecondExampleModel after insertions:")
    linked_list.print_list()

    linked_list.delete_node(node_3)

    print(f"\nLinked List after deletion of {node_3.value}:")
    linked_list.print_list()


def main() -> None:
    for example in (first_example, second_example):
        print(f"\nRunning {example.__name__}...")
        example()


if __name__ == "__main__":
    main()

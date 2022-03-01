from typing import TypeVar, Generic, Optional
from linked_list_node import ListNode as Node


T = TypeVar('T')


class LinkedList(Generic[T]):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, val: T):
        node = Node(val)
        if self.head is None:
            self.tail = node
        else:
            node.next = self.head
        self.head = node

    def insert_at_tail(self, val: T):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def find(self, target: T) -> Optional[Node]:
        if self.head is None:
            return None
        else:
            node = self.head
            while node is not None:
                if node.val == target:
                    return node
                node = node.next
            return None

    def insert(self, target: T, val: T):
        t = self.find(target)
        if t is None:
            return
        node = Node(val)
        if t is self.tail:
            self.tail = node
        node.next = t.next
        t.next = node

    def delete(self, target: T) -> Optional[Node]:
        if self.head is None:
            return
        curr = self.head
        if curr.val == target:
            # Delete head
            if curr.next is None:
                # Delete the list since it hgs only one node.
                self.delete_list()
            else:
                self.head = curr.next
            return
        while curr.next is not None:
            if curr.next.val == target:
                if curr.next is self.tail:
                    # Delete tail
                    self.tail = curr
                curr.next = curr.next.next
                break
            curr = curr.next

    def get_mid(self) -> Optional[Node]:
        if self.head is None:
            return None
        fast = slow = self.head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def delete_list(self):
        self.head = None
        self.tail = None

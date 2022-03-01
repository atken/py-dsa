from typing import TypeVar, Generic, Optional
from linked_list_node import ListNode as Node


T = TypeVar('T')


class CircularLinkedList(Generic[T]):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_to_empty(self, val: T):
        node = Node(val)
        self.head = node.next = self.tail = node

    def insert_at_head(self, val: T):
        if self.head is None:
            self.insert_to_empty(val)
        else:
            node = Node(val)
            node.next = self.head
            self.head = self.tail.next = node

    def insert_at_tail(self, val: T):
        if self.tail is None:
            self.insert_to_empty(val)
        else:
            node = Node(val)
            self.tail.next = node
            self.tail = node
            node.next = self.head

    def find(self, target: T) -> Optional[Node]:
        if self.head is None:
            return None
        node = self.head
        while True:
            if node.val == target:
                return node
            node = node.next
            if node is self.head:
                return None

    def insert(self, target: T, val: T):
        t = self.find(target)
        if t is None:
            return
        if t is self.tail:
            self.insert_at_tail(val)
        else:
            node = Node(val)
            node.next = t.next
            t.next = node
    
    def delete(self, target: T) -> Optional[Node]:
        if self.head is None:
            return
        curr = self.head
        if curr.val == target:
            # Delete head
            if curr.next is self.head:
                # Delete the list since it hgs only one node.
                self.delete_list()
            else:
                self.head = self.tail.next = curr.next
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
        while fast.next is not self.head and fast.next.next is not self.head:
            fast = fast.next.next
            slow = slow.next
        return slow

    def delete_list(self):
        self.head = None
        self.tail = None

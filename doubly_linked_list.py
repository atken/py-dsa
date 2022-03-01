from typing import TypeVar, Generic, Optional
from linked_list_node import DoublyListNode as Node


T = TypeVar('T')


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, val: T):
        node = Node(val)
        if self.head is None:
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node 
        self.head = node

    def insert_at_tail(self, val: T):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            node.prev = self.tail
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
        if t is self.tail:
            self.insert_at_tail(val)
        else:
            # After head or mid
            node = Node(val, prv=t, nxt=t.next)
            t.next.prev = node
            t.next = node

    def delete(self, target: T) -> Optional[Node]:
        if self.head is None:
            return
        curr = self.head
        while curr is not None:
            if curr.val == target:
                if curr is self.head:
                    # Delete head
                    if curr.next is None:
                        # Delete the list since it hgs only one node.
                        self.delete_list()
                    else:
                        self.head = curr.next
                        curr.next.prev = None
                elif curr is self.tail:
                    # Delete tail
                    self.tail = curr.prev
                    curr.prev.next = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
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

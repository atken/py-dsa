from typing import TypeVar, Generic, Optional
from linked_list_node import DoublyListNode as Node


T = TypeVar('T')


class CircularDoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, val: T):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node.next = node.prev = node
        else:
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.head = node
            self.tail.next = node
    
    def insert_at_tail(self, val: T):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node.next = node.prev = node
        else:
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
            self.tail = node
            self.head.prev = node

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
        elif t is self.tail:
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
                    if self.head is self.tail :
                        # Delete the list since it hgs only one node.
                        self.delete_list()
                    else:
                        self.head = self.tail.next = curr.next
                        curr.next.prev = self.tail
                        curr.next = None
                elif curr is self.tail:
                    # Delete tail
                    self.head.prev = self.tail = curr.prev
                    curr.prev.next = self.head
                    curr.prev = None
                else:
                    # Delete mid
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
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

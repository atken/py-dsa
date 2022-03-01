from typing import TypeVar, Generic


T = TypeVar('T', int, str)


class ListNode(Generic[T]):
    def __init__(self, val: T, nxt=None):
        self.val = val
        self.next = nxt


class DoublyListNode(ListNode[T]):
    def __init__(self, val: T, prv=None, nxt=None):
        super().__init__(val, nxt)
        self.prev = prv

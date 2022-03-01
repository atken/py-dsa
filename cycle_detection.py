from typing import Optional
from linked_list_node import ListNode as Node


def detect_array_cycle(nums: int) -> int:
    """
    Floyd's cycle-finding algorithm
    
    Constraints
    - nums.length == n + 1
    - 1 <= nums[i] <= n
    - All the integers in nums appear only once except for precisely one integer which appears two or more times.
    """
    slow = nums[0]
    fast = nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


def detect_linked_list_cycle(head: Node) -> Optional[Node]:
    # Floyd's cycle-finding algorithm
    if head is None or head.next is None or head.next.next is None:
        return None
    slow = head.next
    fast = head.next.next
    while fast != slow:
        if fast.next is None or fast.next.next is None:
            return None
        slow = slow.next
        fast = fast.next.next
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

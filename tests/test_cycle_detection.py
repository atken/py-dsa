from cycle_detection import detect_array_cycle, detect_linked_list_cycle
from linked_list_node import ListNode as Node 


def test_detect_array_cycle():
    a = [1, 3, 2, 4, 5, 3, 6]
    assert detect_array_cycle(a) == 3

    a = [1, 1]
    assert detect_array_cycle(a) == 1

def test_detect_linked_list_cycle():
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    intersection = head.next.next
    tail = head.next.next.next.next
    tail.next = intersection

    assert detect_linked_list_cycle(head).val == 3

def test_detect_linked_list_cycle_not_found():
    head = Node(1)
    
    assert detect_linked_list_cycle(head) is None

    head.next = Node(2)

    assert detect_linked_list_cycle(head) is None
   
    head.next.next = Node(3)
    
    assert detect_linked_list_cycle(head) is None

    head.next.next.next = Node(4, Node(5))

    assert detect_linked_list_cycle(head) is None


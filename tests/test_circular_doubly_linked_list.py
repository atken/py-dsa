from circular_doubly_linked_list import CircularDoublyLinkedList


def test_insert_at_head():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    
    assert ll.head.val == 1
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 3
    assert ll.head.next.next.next.val == 1
    assert ll.tail.val == 3
    assert ll.tail.prev.val == 2
    assert ll.tail.prev.prev.val == 1
    assert ll.tail.prev.prev.prev.val == 3

def test_insert_at_tail():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()
    ll.insert_at_tail(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    
    assert ll.head.val == 1
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 3
    assert ll.head.next.next.next.val == 1
    assert ll.tail.val == 3
    assert ll.tail.prev.val == 2
    assert ll.tail.prev.prev.val == 1
    assert ll.tail.prev.prev.prev.val == 3

def test_find():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    
    assert ll.find(2) is ll.head.next

def test_not_found():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()

    assert ll.find(1) is None
    
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)

    assert ll.find(4) is None

def test_insert_after_head():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    ll.insert(1, 4)
    
    assert ll.head.val == 1
    assert ll.head.next.val == 4
    assert ll.head.next.next.val == 2
    assert ll.head.next.next.next.val == 3
    assert ll.tail.val == 3
    assert ll.tail.prev.val == 2
    assert ll.tail.prev.prev.val == 4
    assert ll.tail.prev.prev.prev.val == 1

def test_insert_after_mid():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    ll.insert(2, 4)
    
    assert ll.head.val == 1
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 4
    assert ll.head.next.next.next.val == 3
    assert ll.tail.val == 3
    assert ll.tail.prev.val == 4
    assert ll.tail.prev.prev.val == 2
    assert ll.tail.prev.prev.prev.val == 1

def test_insert_after_tail():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    ll.insert(3, 4)
    
    assert ll.head.val == 1
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 3
    assert ll.head.next.next.next.val == 4
    assert ll.tail.val == 4
    assert ll.tail.prev.val == 3
    assert ll.tail.prev.prev.val == 2
    assert ll.tail.prev.prev.prev.val == 1

def test_insert_not_found():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    ll.insert(4, 5)
    
    assert ll.head.val == 1
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 3
    assert ll.tail.val == 3
    assert ll.tail.prev.val == 2
    assert ll.tail.prev.prev.val == 1

def test_delete_head():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    ll.delete(1)
    
    assert ll.head.val == 2
    assert ll.head.next.val == 3
    assert ll.head.next.next.val == 2
    assert ll.tail.val == 3
    assert ll.tail.prev.val == 2
    assert ll.tail.prev.prev.val == 3

def test_delete_mid():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    ll.delete(2)
    
    assert ll.head.val == 1
    assert ll.head.next.val == 3
    assert ll.head.next.next.val == 1
    assert ll.tail.val == 3
    assert ll.tail.prev.val == 1
    assert ll.tail.prev.prev.val == 3

def test_delete_tail():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    ll.delete(3)
    
    assert ll.head.val == 1
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 1
    assert ll.tail.val == 2
    assert ll.tail.prev.val == 1
    assert ll.tail.prev.prev.val == 2

def test_delete_empty():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()
    ll.delete(1)

    assert ll.head is None
    assert ll.tail is None

def test_delete_node_then_delete_list():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList() 
    ll.insert_at_tail(1)
    ll.delete(1)

    assert ll.head is None
    assert ll.tail is None

def test_get_mid():
    ll: CircularDoublyLinkedList[int] = CircularDoublyLinkedList()

    assert ll.get_mid() is None
    
    ll.insert_at_tail(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_tail(4)

    assert ll.get_mid().val == 2
    
    ll.insert_at_tail(5)
    
    assert ll.get_mid().val == 3


from post_order_traversal import Node, traverse, traverse_2 


def test_traverse():
    root_node = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
    assert traverse(root_node) == [3, 4, 2, 6, 7, 5, 1]
    assert traverse_2(root_node) == [3, 4, 2, 6, 7, 5, 1]


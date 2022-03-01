from morris_traversal import in_order_traverse, pre_order_traverse, post_order_traverse
from binary_tree_node import BinaryTreeNode as Node


def test_in_order_traverse():
    root_node = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
    assert in_order_traverse(root_node) == [3, 2, 4, 1, 6, 5, 7]

def test_pre_order_traverse():
    root_node = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
    assert pre_order_traverse(root_node) == [1, 2, 3, 4, 5, 6, 7]

def test_post_order_traverse():
    root_node = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
    assert post_order_traverse(root_node) == [3, 4, 2, 6, 7, 5, 1]


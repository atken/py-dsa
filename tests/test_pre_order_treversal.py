from pre_order_traversal import traverse, traverse_2 
from binary_tree_node import BinaryTreeNode as Node


def test_traverse():
    root_node = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
    assert traverse(root_node) == [1, 2, 3, 4, 5, 6, 7]
    assert traverse_2(root_node) == [1, 2, 3, 4, 5, 6, 7]


from level_order_traversal import traverse, traverse_2 
from binary_tree_node import BinaryTreeNode as Node


def test_traverse():
    root_node = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
    
    assert traverse(root_node) == [[1], [2, 5], [3, 4, 6, 7]]
    assert traverse_2(root_node) == [[1], [2, 5], [3, 4, 6, 7]]

def test_traverse_unbalanced():
    root_node = Node(1, Node(2, Node(3, Node(4))), Node(5, None, Node(6)))
    
    assert traverse(root_node) == [[1], [2, 5], [3, 6], [4]]
    assert traverse_2(root_node) == [[1], [2, 5], [3, 6], [4]]

def test_traverse_empty():
    assert traverse(None) == []
    assert traverse_2(None) == []


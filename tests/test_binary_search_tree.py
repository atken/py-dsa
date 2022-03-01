from binary_search_tree import BinarySearchTree


def test_insert():
    r"""
        5
       / \
      3   7
     / \   \
    1   4   9
    """
    tree = BinarySearchTree()
    root = tree.insert(None, 5)
    root = tree.insert(root, 3)
    root = tree.insert(root, 1)
    root = tree.insert(root, 4)
    root = tree.insert(root, 7)
    root = tree.insert(root, 7)  # Skipped
    root = tree.insert(root, 9)
    
    assert root.val == 5
    assert root.left.val == 3
    assert root.right.val == 7
    assert root.left.left.val == 1
    assert root.left.right.val == 4
    assert root.right.left is None
    assert root.right.right.val == 9
    assert root.left.left.left is None
    assert root.left.left.right is None
    assert root.left.right.left is None
    assert root.left.right.right is None
    assert root.right.left is None
    assert root.right.right.val == 9
    assert root.right.right.left is None
    assert root.right.right.right is None

def test_insert_unbalanced():
    r"""
    5
     \
      7
       \
        9
    """
    tree = BinarySearchTree()
    root = tree.insert(None, 5)
    root = tree.insert(root, 7)
    root = tree.insert(root, 9)

    assert root.val == 5
    assert root.left is None
    assert root.right.val == 7
    assert root.right.left is None
    assert root.right.right.val == 9
    assert root.right.right.left is None
    assert root.right.right.right is None

def test_delete_leaf():
    r"""
      3         3          3
     / \   ->    \    ->      ->
    1   5         5
    """
    tree = BinarySearchTree()
    root = tree.insert(None, 3)
    root = tree.insert(root, 1)
    root = tree.insert(root, 5)
    root = tree.delete(root, 1)
    
    assert root.val == 3
    assert root.left is None
    assert root.right.val == 5

    root = tree.delete(root, 5)

    assert root.val == 3
    assert root.left is None
    assert root.right is None

    root = tree.delete(root, 3)

    assert root is None
    assert tree.delete(root, 1) is None
    
def test_delete_not_leaf():
    r"""
        5              5             5            5
       / \            / \           / \          / \
      2   7    ->    3   7    ->   4   7    ->  1   7
     / \   \        / \   \       /     \            \
    1   4   9      1   4   9     1       9            9
       / 
      3
    """
    tree = BinarySearchTree()
    root = tree.insert(None, 5)
    root = tree.insert(root, 2)
    root = tree.insert(root, 7)
    root = tree.insert(root, 1)
    root = tree.insert(root, 4)
    root = tree.insert(root, 9)
    root = tree.insert(root, 3)
    root = tree.delete(root, 2)
    
    assert root.val == 5
    assert root.left.val == 3
    assert root.right.val == 7
    assert root.left.left.val == 1
    assert root.left.right.val == 4
    assert root.right.left is None
    assert root.right.right.val == 9

    root = tree.delete(root, 3)
    
    assert root.val == 5
    assert root.left.val == 4
    assert root.right.val == 7
    assert root.left.left.val == 1
    assert root.left.right is None
    assert root.right.left is None
    assert root.right.right.val == 9

    root = tree.delete(root, 4)
    
    assert root.val == 5
    assert root.left.val == 1
    assert root.right.val == 7
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left is None
    assert root.right.right.val == 9


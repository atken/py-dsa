from avl_tree import AVLTree


def test_insert_left_left():
    r"""
          4          4 
         / \        / \
       '3'  5  ->  2   5
       /          / \
      2          1   3  
     /
    1
    """
    tree = AVLTree()
    root = tree.insert(None, 4)
    root = tree.insert(root, 3)
    root = tree.insert(root, 5)
    root = tree.insert(root, 2)
    root = tree.insert(root, 1)
    
    assert root.val == 4
    assert root.left.val == 2
    assert root.right.val == 5
    assert root.left.left.val == 1
    assert root.left.right.val == 3
    assert root.right.left is None
    assert root.right.right is None
    
def test_insert_left_left_2():
    r"""
         '5'         3 
         / \        / \
        3   6  ->  2   5
       / \        /   / \
      2   4      1   4   6
     /
    1
    """
    tree = AVLTree()
    root = tree.insert(None, 5)
    root = tree.insert(root, 3)
    root = tree.insert(root, 2)
    root = tree.insert(root, 4)
    root = tree.insert(root, 6)
    root = tree.insert(root, 1)
    
    assert root.val == 3
    assert root.left.val == 2
    assert root.right.val == 5
    assert root.left.left.val == 1
    assert root.left.right is None
    assert root.right.left.val == 4
    assert root.right.right.val == 6

def test_insert_left_left_3():
    r"""
       '5'         3
       / \        / \ 
      3   6  ->  1   5
     / \          \ / \
    1   4         2 4  6
         \ 
          2 
    """
    tree = AVLTree()
    root = tree.insert(None, 5)
    root = tree.insert(root, 3)
    root = tree.insert(root, 6)
    root = tree.insert(root, 1)
    root = tree.insert(root, 4)
    root = tree.insert(root, 2)
    
    assert root.val == 3
    assert root.left.val == 1
    assert root.right.val == 5
    assert root.left.left is None
    assert root.left.right.val == 2
    assert root.right.left.val == 4
    assert root.right.right.val == 6

def test_insert_right_right():
    r"""
      2           2 
     / \         / \
    1  '3'  ->  1   4
         \         / \
          4       3   5
           \
            5
    """
    tree = AVLTree()
    root = tree.insert(None, 2)
    root = tree.insert(root, 1)
    root = tree.insert(root, 3)
    root = tree.insert(root, 4)
    root = tree.insert(root, 5)
    
    assert root.val == 2
    assert root.left.val == 1
    assert root.right.val ==4
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left.val == 3
    assert root.right.right.val == 5

def test_insert_right_right_2():
    r"""
      '2'           4 
      / \          / \
     1   4  ->    2   5 
        / \      / \   \
       3   5    1   3   6
            \
             6
    """
    tree = AVLTree()
    root = tree.insert(None, 2)
    root = tree.insert(root, 1)
    root = tree.insert(root, 4)
    root = tree.insert(root, 3)
    root = tree.insert(root, 5)
    root = tree.insert(root, 6)
    
    assert root.val == 4
    assert root.left.val == 2
    assert root.right.val == 5
    assert root.left.left.val == 1
    assert root.left.right.val == 3
    assert root.right.left is None
    assert root.right.right.val == 6

def test_insert_left_right():
    r"""
        4            4           4
       / \          / \         / \
     '3'  5  ->   '3'  5  ->   2   5
     /            /           / \
    1            2           1   3
     \          / 
      2        1
    """
    tree = AVLTree()
    root = tree.insert(None, 4)
    root = tree.insert(root, 3)
    root = tree.insert(root, 5)
    root = tree.insert(root, 1)
    root = tree.insert(root, 2)
    
    assert root.val == 4
    assert root.left.val == 2
    assert root.right.val == 5
    assert root.left.left.val == 1
    assert root.left.right.val == 3
    assert root.right.left is None
    assert root.right.right is None

def test_insert_right_left():
    r"""
      2            2           2
     / \          / \         / \
    1  '4'   ->  1  '4'  ->  1   5
         \            \         / \
          6            5       4   6
         /              \
        5                6  
    """
    tree = AVLTree()
    root = tree.insert(None, 2)
    root = tree.insert(root, 1)
    root = tree.insert(root, 4)
    root = tree.insert(root, 6)
    root = tree.insert(root, 5)
    
    assert root.val == 2
    assert root.left.val == 1
    assert root.right.val == 5
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left.val == 4
    assert root.right.right.val == 6

def test_delete_leaf_left_left():
    r"""
        4         '4'        2
       / \        /         / \
      2   5  ->  2    ->   1   4
     /          /
    1          1 
    """
    tree = AVLTree()
    root = tree.insert(None, 4)
    root = tree.insert(root, 2)
    root = tree.insert(root, 5)
    root = tree.insert(root, 1)
    root = tree.delete(root, 5)
    
    assert root.val == 2
    assert root.left.val == 1
    assert root.right.val == 4
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left is None
    assert root.right.right is None

def test_delete_leaf_left_left_2():
    r"""
        4         '4'        2
       / \        /         / \
      2   5  ->  2    ->   1   4
     / \        / \           /
    1   3      1   3         3
    """
    tree = AVLTree()
    root = tree.insert(None, 4)
    root = tree.insert(root, 2)
    root = tree.insert(root, 5)
    root = tree.insert(root, 1)
    root = tree.insert(root, 3)
    root = tree.delete(root, 5)
    
    assert root.val == 2
    assert root.left.val == 1
    assert root.right.val == 4
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left.val == 3
    assert root.right.right is None

def test_delete_not_leaf_left_left():
    r"""
        4         '5'       2   
       / \        /        / \
      2   5  ->  2    ->  1   5
     / \        / \          /
    1   3      1   3        3
    """
    tree = AVLTree()
    root = tree.insert(None, 4)
    root = tree.insert(root, 2)
    root = tree.insert(root, 5)
    root = tree.insert(root, 1)
    root = tree.insert(root, 3)
    root = tree.delete(root, 4)
    
    assert root.val == 2
    assert root.left.val == 1
    assert root.right.val == 5
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left.val == 3
    assert root.right.right is None

def test_delete_not_leaf_left_left_2():
    r"""
          4           5           5  
         / \         / \         / \
        3   6  ->  '3'  6  ->   2   6
       /   /       /           / \ 
      2   5       2           1   3
     /           /
    1           1
    """
    tree = AVLTree()
    root = tree.insert(None, 4)
    root = tree.insert(root, 3)
    root = tree.insert(root, 6)
    root = tree.insert(root, 2)
    root = tree.insert(root, 5)
    root = tree.insert(root, 1)
    root = tree.delete(root, 4)
    
    assert root.val == 5
    assert root.left.val == 2
    assert root.right.val == 6
    assert root.left.left.val == 1
    assert root.left.right.val == 3
    assert root.right.left is None
    assert root.right.right is None

def test_delete_leaf_left_right():
    r"""
      4         '4'       '4'       3
     / \        /         /        / \
    2   5  ->  2    ->   3    ->  2   4
     \          \       /
      3          3     2
    """
    tree = AVLTree()
    root = tree.insert(None, 4)
    root = tree.insert(root, 2)
    root = tree.insert(root, 5)
    root = tree.insert(root, 3)
    root = tree.delete(root, 5)
    
    assert root.val == 3
    assert root.left.val == 2
    assert root.right.val == 4
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left is None
    assert root.right.right is None

def test_delete_not_leaf_left_right():
    r"""
        5          '5'         '5'         3 
       / \         / \         / \        / \
      2   6   ->  2   7  ->   3   7  ->  2   5
     / \   \     / \         / \        /   / \
    1   3   7   1   3       2   4      1   4   7
         \           \     /
          4           4   1
    """
    tree = AVLTree()
    root = tree.insert(None, 5)
    root = tree.insert(root, 2)
    root = tree.insert(root, 6)
    root = tree.insert(root, 1)
    root = tree.insert(root, 3)
    root = tree.insert(root, 7)
    root = tree.insert(root, 4)
    root = tree.delete(root, 6)
    
    assert root.val == 3
    assert root.left.val == 2
    assert root.right.val == 5
    assert root.left.left.val == 1
    assert root.left.right is None
    assert root.right.left.val == 4
    assert root.right.right.val == 7

def test_delete_leaf_right_right():
    r"""
      2        '2'           3
     / \         \          / \
    1   3  ->     3   ->   2   4
         \         \
          4         4
    """
    tree = AVLTree()
    root = tree.insert(None, 2)
    root = tree.insert(root, 1)
    root = tree.insert(root, 3)
    root = tree.insert(root, 4)
    root = tree.delete(root, 1)
    
    assert root.val == 3
    assert root.left.val == 2
    assert root.right.val == 4
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left is None
    assert root.right.right is None

def test_delete_leaf_right_right_2():
    r"""
      2        '2'           4
     / \         \          / \
    1   4  ->     4   ->   2   5
       / \       / \        \
      3   5     3   5        3
    """
    tree = AVLTree()
    root = tree.insert(None, 2)
    root = tree.insert(root, 1)
    root = tree.insert(root, 4)
    root = tree.insert(root, 3)
    root = tree.insert(root, 5)
    root = tree.delete(root, 1)
    
    assert root.val == 4
    assert root.left.val == 2
    assert root.right.val == 5
    assert root.left.left is None
    assert root.left.right.val == 3
    assert root.right.left is None
    assert root.right.right is None

def test_delete_not_leaf_right_right():
    r"""
      2          3
     / \        / \
    1   3  ->  1   4
         \          
          4          
    """
    tree = AVLTree()
    root = tree.insert(None, 2)
    root = tree.insert(root, 1)
    root = tree.insert(root, 3)
    root = tree.insert(root, 4)
    root = tree.delete(root, 2)
    
    assert root.val == 3
    assert root.left.val == 1
    assert root.right.val == 4

def test_delete_leaf_right_left():
    r"""
      2        '2'      '2'         3
     / \         \        \        / \
    1   4  ->     4  ->    3  ->  2   4
       /         /          \  
      3         3            4
    """
    tree = AVLTree()
    root = tree.insert(None, 2)
    root = tree.insert(root, 1)
    root = tree.insert(root, 4)
    root = tree.insert(root, 3)
    root = tree.delete(root, 1)
    
    assert root.val == 3
    assert root.left.val == 2
    assert root.right.val == 4

def test_delete_not_leaf_right_left():
    r"""
        3          '3'        '3'          5 
       / \         / \        / \         / \
      2   6   ->  1   6  ->  1   5   ->  3   6
     /   / \         / \        / \     / \   \
    1   5   7       5   7      4   6   1   4   7
       /           /                \
      4           4                  7
    """
    tree = AVLTree()
    root = tree.insert(None, 3)
    root = tree.insert(root, 2)
    root = tree.insert(root, 6)
    root = tree.insert(root, 1)
    root = tree.insert(root, 5)
    root = tree.insert(root, 7)
    root = tree.insert(root, 4)
    root = tree.delete(root, 2)
    
    assert root.val == 5
    assert root.left.val == 3
    assert root.right.val == 6
    assert root.left.left.val == 1
    assert root.left.right.val == 4
    assert root.right.left is None
    assert root.right.right.val == 7

def test_insert_duplicated():
    tree = AVLTree()
    root = tree.insert(None, 2)
    root = tree.insert(root, 1)
    root = tree.insert(root, 3)
    root = tree.insert(root, 1)

    assert root.val == 2
    assert root.left.val == 1
    assert root.right.val == 3
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left is None
    assert root.right.right is None

def test_delete_from_empty():
    tree = AVLTree()
    root = tree.delete(None, 1)

    assert root is None

def test_get_min_node():
    r"""
        3  
       / \
      2   6
     /   / \
    1   5   7
       / 
      4
    """
    tree = AVLTree()
    root = tree.insert(None, 3)
    root = tree.insert(root, 2)
    root = tree.insert(root, 6)
    root = tree.insert(root, 1)
    root = tree.insert(root, 5)
    root = tree.insert(root, 7)
    root = tree.insert(root, 4)

    assert tree.get_min_node(root.right).val == 4


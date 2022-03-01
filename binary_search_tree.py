from typing import List, Optional
from binary_tree_node import BinaryTreeNode as Node


class BinarySearchTree:
    def get_min_node(self, root: Node) -> Optional[Node]:
        if root is None or root.left is None:
            return root
        return self.get_min_node(root.left)

    def insert(self, root: Node, val: int) -> Node:
        if root is None:
            return Node(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        else:
            print('{} is already exists in this tree.'.format(val))
            return root
        return root

    
    def delete(self, root: Node, val: int) -> Optional[Node]:
        if root is None:
            return None
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                right_sub_min = self.get_min_node(root.right)
                root.val = right_sub_min.val
                root.right = self.delete(root.right, right_sub_min.val)
        return root


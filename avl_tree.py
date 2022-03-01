from typing import List, Optional
from binary_tree_node import BinaryTreeNode as Node


class AVLTree:
    def get_height(self, root: Node) -> int:
        return 0 if root is None else root.height

    def get_balance(self, root: Node) -> int:
        return 0 if root is None else self.get_height(root.left) - self.get_height(root.right)

    def get_min_node(self, root: Node) -> Optional[Node]:
        if root is None or root.left is None:
            return root
        return self.get_min_node(root.left)

    def rotate_right(self, old_root: Node) -> Node:
        new_root = old_root.left
        tmp = new_root.right
        new_root.right = old_root
        old_root.left = tmp
        old_root.height = 1 + max(self.get_height(old_root.left), self.get_height(old_root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(old_root.right))
        return new_root

    def rotate_left(self, old_root: Node) -> Node:
        new_root = old_root.right
        tmp = new_root.left
        new_root.left = old_root
        old_root.right = tmp
        old_root.height = 1 + max(self.get_height(old_root.left), self.get_height(old_root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

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

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left-Left condition
        if balance > 1 and val < root.left.val:
            return self.rotate_right(root)

        # Left-Right condition
        if balance > 1 and val > root.left.val:
            root.left = self.rotate_left(root.left)  # Transform to Left-Left condition.
            return self.rotate_right(root)

        # Right-Right condition
        if balance < -1 and val > root.right.val:
            return self.rotate_left(root)

        # Right-Left condition
        if balance < -1 and val < root.right.val:
            root.right = self.rotate_right(root.right)  # Transform to Right-Right condition.
            return self.rotate_left(root)

        return root

    def delete(self, root: Node, val: int) -> Optional[Node]:
        if root is None:
            return None 
        elif val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                tmp = self.get_min_node(root.right)
                root.val = tmp.val
                root.right = self.delete(root.right, tmp.val)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left-Left condition
        # Left subtree is left-biased or perfectly balanced
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        # Left-Right condition
        # Left subtree is right-biased
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right-Right condition
        # Right subtree is right-biased or perfectly balanced
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        # Right-Left condition
        # Right subtree is left-biased
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root


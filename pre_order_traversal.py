from typing import List
from binary_tree_node import BinaryTreeNode as Node


def traverse(root: Node) -> List[int]:
    # Recursive
    ans = []
    if root is not None:
        ans.append(root.val)
        ans += traverse(root.left)
        ans += traverse(root.right)
    return ans


def traverse_2(root: Node) -> List[int]:
    # Iterative
    ans = []
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        ans.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return ans


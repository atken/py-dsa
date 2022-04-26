from typing import List
from binary_tree_node import BinaryTreeNode as Node


def traverse(root: Node) -> List[int]:
    # Recursive
    ans = []
    if root:
        ans += traverse(root.left)
        ans.append(root.val)
        ans += traverse(root.right)
    return ans


def traverse_2(root: Node) -> List[int]:
    # Iterative
    ans = []
    stack = []
    current = root
    while current is not None or len(stack) > 0:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        ans.append(current.val)
        current = current.right
    return ans


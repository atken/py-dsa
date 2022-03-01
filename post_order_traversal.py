from typing import List, Optional
from binary_tree_node import BinaryTreeNode as Node


def traverse(root: Node) -> List[int]:
    # Recursive
    ans = []
    if root:
        ans += traverse(root.left)
        ans += traverse(root.right)
        ans.append(root.val)
    return ans


def traverse_2(root: Node) -> List[int]:
    # Iterative
    def peek(st: List[int]) -> Optional[int]:
        return st[-1] if len(st) > 0 else None

    ans = []
    stack = []
    while True:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.right and peek(stack) == root.right:
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            ans.append(root.val)
            root = None
        if len(stack) < 1:
            break
    return ans


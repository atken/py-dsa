from typing import List
from binary_tree_node import BinaryTreeNode as Node


def traverse(root: Node) -> List[List[int]]:
    # Recursive
    def helper(rt: Node, level: int) -> None:
        if rt is None:
            return
        if level >= len(ans):
            ans.append([])
        ans[level].append(rt.val)
        helper(rt.left, level + 1)
        helper(rt.right, level + 1)

    ans = []
    helper(root, 0)
    return ans


def traverse_2(root: Node) -> List[List[int]]:
    # Iterative
    if root is None:
        return []
    ans, level = [], [root]
    while len(level) > 0:
        ans.append([node.val for node in level])  # Grouped by level (e.g. ans = [[1] [2, 3], [4, 5, 6, 7]])
        # ans.extend([node.val for node in level])
        lr_pairs = [(node.left, node.right) for node in level]
        level = [node for lr_pair in lr_pairs for node in lr_pair if node]
    return ans

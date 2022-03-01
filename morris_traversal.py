from typing import List
from binary_tree_node import BinaryTreeNode as Node


def in_order_traverse(root: Node) -> List[int]:
    ans = []
    curr = root
    while curr is not None:
        if curr.left is None:
            ans.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right is not None and prev.right is not curr:
                prev = prev.right
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                ans.append(curr.val)
                curr = curr.right
    return ans

def pre_order_traverse(root: Node) -> List[int]:
    ans = []
    curr = root
    while curr is not None:
        if curr.left is None:
            ans.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right is not None and prev.right is not curr:
                prev = prev.right
            if prev.right is curr:
                prev.right = None
                curr = curr.right
            else:
                ans.append(curr.val)
                prev.right = curr
                curr = curr.left
    return ans

def post_order_traverse(root: Node) -> List[int]:
    ans = []
    curr = Node(-1)  # Dummy node
    prev = None
    prev2 = None
    succ = None
    curr.left = root
    while curr is not None:
        if curr.left is None:
            curr = curr.right
        else:
            prev = curr.left
            while prev.right is not None and prev.right is not curr:
                prev = prev.right
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                succ = curr
                curr = curr.left
                prev2 = None
                while curr is not None:
                    temp = curr.right
                    curr.right = prev2
                    prev2 = curr
                    curr = temp
                while prev2 is not None:
                    ans.append(prev2.val)
                    temp = prev2.right
                    prev2.right = curr
                    curr = prev2
                    prev2 = temp
                curr = succ.right
    return ans


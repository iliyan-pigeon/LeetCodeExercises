from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count_nodes = 0

        def inner_func(node):
            count = 0
            if node:
                count += 1
            else:
                return count

            count += inner_func(node.left)
            count += inner_func(node.right)

            return count

        count_nodes += inner_func(root)

        return count_nodes

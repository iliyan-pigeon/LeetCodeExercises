from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []
        current = ""

        def add_path(node, curr):
            curr += str(node.val)

            if not node.left and not node.right:
                numbers.append(int(curr))
                return

            if node.left:
                add_path(node.left, curr)

            if node.right:
                add_path(node.right, curr)

        add_path(root, current)

        return sum(numbers)
    
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        leafs = []

        if not root:
            return False

        def add_sum(node):

            if not node.left and not node.right:
                leafs.append(node.val == targetSum)

            prev_val = node.val

            if node.left:
                left_node = node.left
                left_node.val += prev_val
                add_sum(left_node)

            if node.right:
                right_node = node.right
                right_node.val += prev_val
                add_sum(right_node)

        add_sum(root)

        if True in leafs:
            return True

        return False
    
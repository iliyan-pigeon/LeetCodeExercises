from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if node.left or node.right:
                move = node.left
                node.left = node.right
                node.right = move

                if node.left:
                    invert(node.left)
                if node.right:
                    invert(node.right)
        if root:
            invert(root)
        return root
    
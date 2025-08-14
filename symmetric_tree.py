from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []

        def collect_left(node, the_list):
            the_list.append(node.val)

            if node.left:
                collect_left(node.left, the_list)
            else:
                the_list.append(None)
            if node.right:
                collect_left(node.right, the_list)
            else:
                the_list.append(None)

        def collect_right(node, the_list):
            the_list.append(node.val)

            if node.right:
                collect_right(node.right, the_list)
            else:
                the_list.append(None)
            if node.left:
                collect_right(node.left, the_list)
            else:
                the_list.append(None)

        if root.left:
            collect_left(root.left, left)

        if root.right:
            collect_right(root.right, right)

        return left == right

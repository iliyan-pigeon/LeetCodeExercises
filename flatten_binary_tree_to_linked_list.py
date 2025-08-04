from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        rights = []

        while root:
            if root.right is not None:
                rights.append(root.right)

            if root.left is not None:
                root.right = root.left
                root.left = None
            else:
                if rights:
                    root.right = rights.pop()

            root = root.right
            
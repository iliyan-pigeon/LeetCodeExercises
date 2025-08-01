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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        values = []
        while head:
            values.append(head.val)
            head = head.next

        def buildBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(values[mid])
            node.left = buildBST(left, mid - 1)
            node.right = buildBST(mid + 1, right)
            return node

        return buildBST(0, len(values) - 1)
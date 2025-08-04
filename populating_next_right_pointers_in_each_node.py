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


class Node:
    def __init__(self, val: int=0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return

        nodes = [root]

        def inner(n):
            new_nodes = []
            while n:
                if n:
                    current = n.pop(0)
                    if current.left:
                        new_nodes.append(current.left)
                        new_nodes.append(current.right)
                    if n:
                        current.next = n[0]
            return new_nodes

        while nodes:
            nodes.extend(inner(nodes))

        return root
    
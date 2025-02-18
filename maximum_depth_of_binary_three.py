class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Solution 2
from collections import deque


class Solution:
    def maxDepth(self,root):
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()  # Correct BFS processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, paths):
            if node is not None:
                path.append(str(node.val))
                
                # If it's a leaf node, add the path to the paths list
                if node.left is None and node.right is None:
                    paths.append("->".join(path))
                else:
                    # Otherwise, continue the search in the left and right children
                    if node.left:
                        dfs(node.left, path, paths)
                    if node.right:
                        dfs(node.right, path, paths)
                
                # Backtrack: remove the current node from the path
                path.pop()
        
        paths = []
        dfs(root, [], paths)
        return paths
      

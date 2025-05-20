from typing import Optional, List


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
                
                if node.left is None and node.right is None:
                    paths.append("->".join(path))
                else:
                    if node.left:
                        dfs(node.left, path, paths)
                    if node.right:
                        dfs(node.right, path, paths)

                path.pop()
        
        paths = []
        dfs(root, [], paths)
        return paths
      

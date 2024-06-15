# Given a binary tree root, 
# a node X in the tree is named good if in the path 
# from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root) -> int:
        
        def dfs(node, mx):
            if not node:
                return 0
            
            res = 1 if node.val >= mx else 0
            mx = max(mx, node.val)
            res += dfs(node.left, mx) 
            res += dfs(node.right, mx)
            return res
        
        return dfs(root, root.val)
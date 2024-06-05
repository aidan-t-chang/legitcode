# Given the root of a binary tree, 
# return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path 
# between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is 
# represented by the number of edges between them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1 # height of a null node
            left = dfs(root.left) # height of left subtree
            right = dfs(root.right) # height of right subtree

            res[0] = max(res[0], 2 + left + right) # find the max diameter from each node

            return 1 + max(left, right) # return the height running through the root node

        dfs(root)
        return res[0]
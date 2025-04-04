# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

# Recall that:

# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
# The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root):
        
        def dfs(root):
            if not root:
                return 0, None

            left = dfs(root.left)
            right = dfs(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]

            return left[0] + 1, root

        return dfs(root)[1]
            
# A path in a binary tree is a sequence of nodes where each pair 
# of adjacent nodes in the sequence has an edge connecting them. 
# A node can only appear in the sequence at most once. 
# Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, 
# return the maximum path sum of any non-empty path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root) -> int:
        res = [root.val] # array so it can be updated within the dfs function

        #return max path sum without splitting to be recursively worked on
        def dfs(root):
            if not root:
                return 0
            
            leftM = dfs(root.left)
            rightM = dfs(root.right)
            leftM = max(leftM, 0) # make sure value is >= 0
            rightM = max(rightM, 0)

            #compute max path sum WITH split (what could actually be the result)
            res[0] = max(res[0], root.val + leftM + rightM) # computing possible result

            #return value is without the split
            return root.val + max(leftM, rightM)
            # if we choose both left and right, that would mean we are splitting

        dfs(root)
        return res[0]
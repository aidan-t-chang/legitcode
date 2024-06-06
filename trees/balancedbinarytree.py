# Given a binary tree, determine if it is 
# height-balanced.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root) -> bool:

        def dfs(root): # returns boolean and height of tree
            if not root:
                return [True, 0] # balanced with height 0 if the root is null

            left, right = dfs(root.left), dfs(root.right) # call dfs on both subtrees
            balance = left[0] == True and right[0] == True and abs(left[1] - right[1]) <= 1 # calculate the height and see if they are balanced

            return [balance, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
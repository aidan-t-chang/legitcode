# Given the root of a Binary Search Tree (BST), 
# convert it to a Greater Tree such that every key of the 
# original BST is changed to the original key plus 
# the sum of all keys greater than the original key in BST.


class Solution:
    def bstToGst(self, root):
        self.sum = 0
        def dfs(root):
            if root:
                dfs(root.right) # traverse the right subtree first
                self.sum += root.val # update the sum
                root.val = self.sum # update current node value to be the new sum value
                dfs(root.left) # traverse the left subtree last
            return root # return the new tree
        dfs(root)
        return root
# Given the root of a binary tree, 
# determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree
# of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys 
# greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

class Solution:
    def isValidBST(self, root):

        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float('-inf'), float('inf'))
# Given the roots of two binary trees root and subRoot, 
# return true if there is a subtree of root with the same structure and 
# node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a 
# node in tree and all of this node's descendants. 
# The tree tree could also be considered as a subtree of itself.

 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) # dont change t because the subtree doesnt change



    def sameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
    
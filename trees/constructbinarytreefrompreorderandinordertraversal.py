# Given two integer arrays preorder and 
# inorder where preorder is the preorder 
# traversal of a binary tree and inorder is the 
# inorder traversal of the same tree, construct and return the binary tree.



class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
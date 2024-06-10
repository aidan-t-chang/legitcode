# Given a binary search tree (BST) where all node values are unique, 
# and two nodes from the tree p and q, 
# return the lowest common ancestor (LCA) of the two nodes.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        # Iterative search
        while cur:
            if p.val > cur.val and q.val > cur.val: # if both values are larger than the root node, search right
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val: # if both values are smaller than the root node, search left
                cur = cur.left
            else: # only other case is if we have found the LCA
                return cur
# We run a preorder depth-first search (DFS) on the root of a binary tree.

# At each node in this traversal, we output D dashes (where D is the depth of this node), 
# then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  
# The depth of the root node is 0.

# If a node has only one child, that child is guaranteed to be the left child.

# Given the output traversal of this traversal, recover the tree and return its root.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str):
        self.s = traversal
        self.i = 0
        self.level = 0
        node = TreeNode(-1)
        self.helper(node, 0)
        return node.left
    
    def helper(self, parent, lvl):
        while self.i < len(self.s) and lvl == self.level:
            num = 0
            while self.i < len(self.s) and self.s[self.i].isdigit():
                num = num * 10 + int(self.s[self.i])
                self.i += 1
            node = TreeNode(num)
            if not parent.left:
                parent.left = node
            else:
                parent.right = node
            self.level = 0
            while self.i < len(self.s) and self.s[self.i] == "-":
                self.level += 1
                self.i += 1
            self.helper(node, lvl+1)
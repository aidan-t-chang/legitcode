# Given the root of an n-ary tree, 
# return the postorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order 
# traversal. Each group of children is separated by the null value 
# (See examples)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root):
        if not root:
            return []

        res = []
        def dfs(root):
            for child in root.children:
                dfs(child)
            res.append(root.val)
        
        dfs(root)
        return res
            
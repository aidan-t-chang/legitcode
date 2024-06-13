# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q) # get the amount of nodes in the q
            level = []
            for i in range(qLen): # level by level
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        if level:
            res.append(level)
        return res
            
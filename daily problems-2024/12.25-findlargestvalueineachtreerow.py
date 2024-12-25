# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
from collections import deque


class Solution:
    def largestValues(self, root):
        q = deque()
        res = []

        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                temp = q.popleft()
                if temp:
                    level.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            if level:
                res.append(max(level))

        return res
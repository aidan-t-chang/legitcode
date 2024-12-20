# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

# For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.

# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

# The level of a node is the number of edges along the path between it and the root node.

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        q = deque()

        q.append(root)
        level1 = 0

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


            if level1 % 2:
                left, right = 0, len(level) - 1
                while left < right:
                    tt = level[left].val
                    level[left].val = level[right].val
                    level[right].val = tt
                    left += 1
                    right -= 1

            level1 += 1

        return root

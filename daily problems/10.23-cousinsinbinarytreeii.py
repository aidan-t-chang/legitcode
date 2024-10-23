# Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Return the root of the modified tree.

# Note that the depth of a node is the number of edges in the path from the root node to it.

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root):
        level_sum = []

        q = deque([root])
        while q:
            cur_sum = 0
            for node in range(len(q)):
                node = q.popleft()
                cur_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sum.append(cur_sum)

        
        q2 = deque([(root, root.val)])
        level = 0
        while q2:
            for i in range(len(q2)):
                node, val = q2.popleft()
                node.val = level_sum[level] - val

                child_sum = 0
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val

                if node.left:
                    q2.append((node.left, child_sum))
                if node.right:
                    q2.append((node.right, child_sum))
            level += 1
        return root
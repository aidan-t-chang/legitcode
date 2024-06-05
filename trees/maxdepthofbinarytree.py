# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the 
# longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Recursive DFS Solution
    def DFSr(self, root):
        if not root:
            return 0
        
        return 1 + max(self.DFSr(root.left), self.DFSr(root.right))
    
    # Iterative BFS Solution
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        #basically count the number of times the queue is not empty(each level)
        while q:
            for i in range(len(q)): # traverse entire level and add the next level then increase number of levels
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    
    # Iterative DFS Solution
    def maxDepth2(self, root) -> int:
        stack = [[root, 1]]
        res = 0 # if there is a null root node, res will stay 0 because of if statement
        while stack:
            node, depth = stack.pop()

            if node: # prevents anything happening to null nodes in stack
                res = max(depth, res)
                stack.append([node.left, depth + 1]) # might add null nodes to stack
                stack.append([node.right, depth + 1])
        return res
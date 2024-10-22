# You are given the root of a binary tree and a positive integer k.

# The level sum in the tree is the sum of the values of the nodes that are on the same level.

# Return the kth largest level sum in the tree (not necessarily distinct). 
# If there are fewer than k levels in the tree, return -1.

# Note that two nodes are on the same level if they have the same distance from the root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
from collections import deque




class Solution:
    def kthLargestLevelSum(self, root, k: int) -> int:
        # bfs, take every level add to MAXheap, while k pop from heap
        heap = []
        heapq.heapify(heap)

        def bfs(root):
            q = deque()
            q.append(root)

            while q:
                temp = 0
                for i in range(len(q)):
                    node = q.popleft()
                    if node:
                        temp += node.val
                        q.append(node.left)
                        q.append(node.right)
                heapq.heappush(heap, -temp)
        
        bfs(root)
        if k >= len(heap):
            return -1
        
        while k > 1:
            heapq.heappop(heap)
            k -= 1
        
        res = heapq.heappop(heap)
        return -res

# You are given n projects where the ith project 
# has a pure profit profits[i] and a 
# minimum capital of capital[i] is needed to start it.

# Initially, you have w capital. 
# When you finish a project, 
# you will obtain its pure profit and the 
# profit will be added to your total capital.

# Pick a list of at most k distinct 
# projects from given projects to maximize your final capital, 
# and return the final maximized capital.

# The answer is guaranteed to fit in a 32-bit signed integer.

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital):
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        maxHeap = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1
            if not maxHeap:
                break
            w -= heapq.heappop(maxHeap)

        return w
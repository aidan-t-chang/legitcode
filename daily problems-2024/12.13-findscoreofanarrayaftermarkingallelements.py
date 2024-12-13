# You are given an array nums consisting of positive integers.

# Starting with score = 0, apply the following algorithm:

# Choose the smallest integer of the array that is not marked. 
# If there is a tie, choose the one with the smallest index.
# Add the value of the chosen integer to score.
# Mark the chosen element and its two adjacent elements if they exist.
# Repeat until all the array elements are marked.
# Return the score you get after applying the above algorithm.

import heapq

class Solution:
    def findScore(self, nums) -> int:
        res = 0
        marked = [False] * len(nums)

        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
        
        while heap:
            n, i = heapq.heappop(heap)
            if not marked[i]:
                marked[i] = True
                res += n
                if i - 1 >= 0:
                    marked[i-1] = True
                if i + 1 < len(nums):
                    marked[i+1] = True
        return res
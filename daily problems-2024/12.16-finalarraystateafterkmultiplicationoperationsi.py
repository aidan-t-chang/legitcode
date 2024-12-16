# You are given an integer array nums, an integer k, and an integer multiplier.

# You need to perform k operations on nums. In each operation:

# Find the minimum value x in nums. If there are multiple occurrences of the minimum value, 
# select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.
import heapq

class Solution:
    def getFinalState(self, nums, k: int, multiplier: int):
        arr = []
        heapq.heapify(arr)

        for i, n in enumerate(nums):
            heapq.heappush(arr, (n, i))
        
        while k and arr:
            t = heapq.heappop(arr)
            new = (t[0] * multiplier, t[1])
            heapq.heappush(arr, new)
            k -= 1
        
        res = [0] * len(nums)
        while arr:
            j = heapq.heappop(arr)
            res[j[1]] = j[0]

        return res
            
# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray 
# of nums with a sum of at least k. If there is no such subarray, return -1.

# A subarray is a contiguous part of an array.
import heapq


class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        res = float("inf")

        cur_sum = 0
        min_heap = [] # (psum, end_index)

        for r in range(len(nums)):
            cur_sum += nums[r]

            if cur_sum >= k:
                res = min(res, r+1)

            while min_heap and cur_sum - min_heap[0][0] >= k:
                prefix, end_idx = heapq.heappop(min_heap)
                res = min(res, r - end_idx)

            heapq.heappush(min_heap, (cur_sum, r))
                
        return -1 if res == float("inf") else res
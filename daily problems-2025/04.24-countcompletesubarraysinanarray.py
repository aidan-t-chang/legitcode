""" You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array. """
from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums) -> int:
        count = defaultdict(int)
        left = res = 0

        for i in range(len(nums)):
            count[nums[i]] += 1
            while len(count) == len(set(nums)):
                res += len(nums) - i
                count[nums[left]] -= 1
                if not count[nums[left]]:
                    del count[nums[left]]
                left += 1
        return res
                
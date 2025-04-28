""" The score of an array is defined as the product of its sum and its length.

For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

A subarray is a contiguous sequence of elements within an array. """

class Solution:
    def countSubarrays(self, nums, k: int) -> int:
        l = 0
        count = 0
        cursum = 0
        for r in range(len(nums)):
            cursum += nums[r]
            while cursum * (r - l + 1) >= k:
                cursum -= nums[l]
                l += 1
            count += (r - l + 1)
        return count
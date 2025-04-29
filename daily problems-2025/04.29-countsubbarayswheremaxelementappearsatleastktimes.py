""" You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array. """


class Solution:
    def countSubarrays(self, nums, k: int) -> int:
        melem = max(nums)
        maxcount = 0
        res = 0
        l = 0

        for r in range(len(nums)):
            maxcount += 1 if nums[r] == melem else 0
            while maxcount >= k:
                maxcount -= 1 if nums[l] == melem else 0
                l += 1
            res += l
        return res
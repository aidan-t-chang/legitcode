""" Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive). """

class Solution:
    def buildArray(self, nums):
        arr = [0] * len(nums)

        for i in range(len(nums)):
            arr[i] = nums[nums[i]]

        return arr
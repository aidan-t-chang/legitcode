# Given an integer array nums and an integer k, 
# return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that 
# x = n * k. 0 is always a multiple of k.

class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        remainder = {0: -1} # map remainder -> ending index
        total = 0 

        for index, number in enumerate(nums): # index and value at the same time
            total += number # add value to the total
            current_remainder = total % k # remainder of the total
            if current_remainder not in remainder:
                remainder[current_remainder] = index
            elif index - remainder[current_remainder] > 1: # if it is a valid subarray:
                return True
        return False
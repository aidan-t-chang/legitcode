# You are given an array nums of non-negative integers. 
# nums is considered special if there exists a number x 
# such that there are exactly x numbers in nums that are greater than or equal to x.

# Notice that x does not have to be an element in nums.

# Return x if the array is special, otherwise, return -1. 
# It can be proven that if nums is special, the value for x is unique.


class Solution:
    def specialArray(self, nums) -> int:
        nums.sort()
        i = 0
        prev = -1
        num_right = len(nums)
        while i < len(nums):
            if nums[i] == num_right or (prev < num_right < nums[i]):
                return num_right
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            prev = nums[i]
            i += 1
            num_right = len(nums) - i
        return -1
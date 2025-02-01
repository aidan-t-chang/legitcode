# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if (nums[i] % 2 and nums[i+1] % 2) or (not nums[i] % 2 and not nums[i+1] % 2):
                return False

        return True 

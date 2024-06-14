# You are given an integer array nums. 
# In one move, you can pick an index i where 
# 0 <= i < nums.length and increment nums[i] by 1.

# Return the minimum number of moves to make every value in nums unique.

# The test cases are generated so that the answer fits in a 32-bit integer.

from collections import defaultdict


class Solution:
    def minIncrementForUnique(self, nums) -> int:
        nums.sort()
        res = 0

        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                res += 1 + nums[i-1] - nums[i]
                nums[i] = nums[i-1] + 1
        
        return res


# You are given a 0-indexed integer array nums.

# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k]

class Solution:
    def maximumTripletValue(self, nums) -> int:
        res = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res
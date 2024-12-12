# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. 
# The width of such a ramp is j - i.

# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

class Solution:
    def maxWidthRamp(self, nums) -> int:
        stack = []

        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        res = 0

        for i in range(len(nums) - 1, 0, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                res = max(res, i - stack[-1])
                stack.pop()
        return res
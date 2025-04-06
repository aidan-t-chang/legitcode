# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.


class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        maxi = 0

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[maxi]:
                maxi = i
        res = []
        i = maxi
        while i >= 0:
            res.append(nums[i])
            i = prev[i]

        return res

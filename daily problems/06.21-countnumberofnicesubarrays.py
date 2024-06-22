# Given an array of integers nums and an integer k. 
# A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

# 3 pointer sliding window solution

class Solution:
    def numberOfSubarrays(self, nums, k):
        res = 0
        l, m = 0, 0
        odd = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1
            
            while odd > k:
                if nums[l] % 2:
                    odd -= 1
                l += 1
                m = l

            if odd == k:
                while not nums[m] % 2:
                    m += 1
                res += (m - l) + 1
        return res
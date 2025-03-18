# You are given an array nums consisting of positive integers.

# We call a subarray of nums nice if the bitwise AND of every pair of elements that 
# are in different positions in the subarray is equal to 0.

# Return the length of the longest nice subarray.

# A subarray is a contiguous part of an array.

# Note that subarrays of length 1 are always considered nice.

class Solution:
    def longestNiceSubarray(self, nums) -> int:
        mlen = 1

        left = 0
        used = 0

        for r in range(len(nums)):
            while used & nums[r] != 0:
                used ^= nums[left]
                left += 1
            
            used |= nums[r]

            mlen = max(mlen, r-left + 1)
        
        return mlen
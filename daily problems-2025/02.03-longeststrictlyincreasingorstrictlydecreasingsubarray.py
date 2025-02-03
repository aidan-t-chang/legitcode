# You are given an array of integers nums. Return the length of the longest 
# subarray
#  of nums which is either 
# strictly increasing
#  or 
# strictly decreasing
# 

class Solution:
    def longestMonotonicSubarray(self, nums) -> int:
        inc = dec = mlen = 1

        for r in range(len(nums)-1):
            if nums[r+1] > nums[r]:
                inc += 1
                dec = 1
            elif nums[r+1] < nums[r]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1

            mlen = max(mlen, inc, dec)


        return mlen
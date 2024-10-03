# Given an array of positive integers nums, 
# remove the smallest subarray (possibly empty) such 
# that the sum of the remaining elements is divisible by p. 
# It is not allowed to remove the whole array.

# Return the length of the smallest subarray that you need to remove, 
# or -1 if it's impossible.

# A subarray is defined as a contiguous block of elements in the array.

class Solution:
    def minSubarray(self, nums, p: int) -> int:
        s = sum(nums)
        rem = s % p

        if rem == 0:
            return 0

        prefixMod = {0: -1}
        psum = 0
        res = len(nums)

        for i, num in enumerate(nums):
            psum += num
            cur = psum % p
            target = (cur - rem + p) % p

            if target in prefixMod:
                res = min(res, i - prefixMod[target])
            
            prefixMod[cur] = i

        return res if res < len(nums) else -1
# Given an array of integers arr, return the number of subarrays with an odd sum.

# Since the answer can be very large, return it modulo 109 + 7

class Solution:
    def numOfSubarrays(self, arr) -> int:
        # odd - even = odd
        # even - odd = odd
        # odd - odd = even
        # even - even = even
        MOD = 10**9 + 7
        psum = [0]
        odd = 0
        even = 0
        for char in arr:
            if (psum[-1] + char) % 2:
                odd += 1
            else:
                even += 1
            psum.append(psum[-1]+char)

        return (odd * even + odd) % MOD

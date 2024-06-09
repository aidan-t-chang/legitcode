# Given an integer array nums and an integer k, 
# return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.


from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        prefix_sum = 0
        res = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        for n in nums:
            prefix_sum += n
            remain = prefix_sum % k

            res += prefix_count[remain]
            prefix_count[remain] += 1
        return res
# You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. 
# There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 
# (every integer in nums1 is paired with every integer in nums2 exactly once).

# Return the bitwise XOR of all integers in nums3.

class Solution:
    def xorAllNums(self, nums1, nums2) -> int:
        res = 0
        if len(nums1) % 2 == 1:
            for n in nums1:
                res ^= n
        if len(nums2) % 2:
            for n in nums2:
                res ^= n

        return res
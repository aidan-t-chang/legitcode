# Given two integer arrays nums1 and nums2, 
# return an array of their intersection. 
# Each element in the result must appear as many times as it shows in 
# both arrays and you may return the result in any order.

from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
    # O(n * m) solution
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        res = []
        for num in nums2:
            for num1 in nums1:
                if num == num1:
                    res.append(num)
                    nums1.remove(num)
                    break
        return res

class Solution:
    def intersect2(self, nums1, nums2):
        #O(max(n,m)) solution
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        res = []
        count = Counter(nums2)

        for n in nums1:
            if n in count and count[n] != 0:
                res.append(n)
                count[n] -= 1
        return res
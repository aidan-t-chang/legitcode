# You are given two arrays nums1 and nums2 consisting of positive integers.

# You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

# Return the minimum equal sum you can obtain, or -1 if it is impossible

class Solution:
    def minSum(self, nums1, nums2) -> int:
        sum1 = 0
        sum2 = 0
        zero1 = 0
        zero2 = 0

        for n in nums1:
            sum1 += n
            if not n:
                sum1 += 1
                zero1 += 1
    
        for n in nums2:
            sum2 += n
            if not n:
                sum2 += 1
                zero2 += 1
        
        if (zero1 == 0 and sum2 > sum1) or (zero2 == 0 and sum1 > sum2):
            return -1
        return max(sum1, sum2)

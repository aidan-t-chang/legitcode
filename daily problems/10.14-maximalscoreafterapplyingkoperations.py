# You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

# In one operation:

# choose an index i such that 0 <= i < nums.length,
# increase your score by nums[i], and
# replace nums[i] with ceil(nums[i] / 3).
# Return the maximum possible score you can attain after applying exactly k operations.

# The ceiling function ceil(val) is the least integer greater than or equal to val.

import heapq, math


class Solution:
    def maxKelements(self, nums, k):
        n2 = []
        heapq.heapify(n2)
        for num in nums:
            heapq.heappush(n2,num*-1)

        res = 0
        while k > 0:
            temp = heapq.heappop(n2) * -1
            res += temp
            new = math.ceil(temp/3)
            heapq.heappush(n2, new * -1)
            k -= 1
        
        return res



# You are given a 0-indexed integer array nums, and an integer k.

# In one operation, you will:

# Take the two smallest integers x and y in nums.
# Remove x and y from nums.
# Add min(x, y) * 2 + max(x, y) anywhere in the array.
# Note that you can only apply the described operation if nums contains at least two elements.

# Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
import heapq

class Solution:
    def minOperations(self, nums, k: int) -> int:
        res = 0
        heapq.heapify(nums)

        while True:
            check1 = heapq.heappop(nums)
            if nums:
                check2 = heapq.heappop(nums)
            if check1 >= k:
                return res
            add = min(check1, check2) * 2 + max(check1, check2)
            heapq.heappush(nums, add)
            res += 1



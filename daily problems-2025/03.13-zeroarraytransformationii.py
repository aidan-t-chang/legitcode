# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

# Each queries[i] represents the following action on nums:

# Decrement the value at each index in the range [li, ri] in nums by at most vali.
# The amount by which each value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.

# Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, 
# nums becomes a Zero Array. If no such k exists, return -1.

class Solution:
    def minZeroArray(self, nums, queries) -> int:
        def find(nums, queries, k):
            total = 0
            diff = [0] * (len(nums) + 1)

            for q in range(k):
                start, end, val = queries[q]

                diff[start] += val
                diff[end+1] -= val

            for i in range(len(nums)):
                total += diff[i]
                if total < nums[i]:
                    return False
            return True
        
        l, r = 0, len(queries)
        if not find(nums, queries, r):
            return -1

        while l <= r:
            mid = l + (r - l) // 2
            if find(nums, queries, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
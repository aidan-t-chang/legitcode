# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

# You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that 
# subarray
#  nums[fromi..toi] is special or not.

# Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

class Solution:
    def isArraySpecial(self, nums, queries):


        res = [False] * len(queries)
        violating_indices = []

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                violating_indices.append(i)

        for i in range(len(queries)):
            query = queries[i]
            start = query[0]
            end = query[1]

            found = self.binsearch(start+1, end, violating_indices)

            if found:
                res[i] = False
            else:
                res[i] = True
        return res

    def binsearch(self, start, end, violating):
        left = 0
        right = len(violating) - 1
        while left <= right:
            mid = left + (right - left) + 1 // 2
            idx = violating[mid]

            if idx < start:
                left = mid + 1
            elif idx > end:
                right = mid - 1
            else:
                return True
        return False


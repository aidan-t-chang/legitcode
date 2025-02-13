# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, 
# and the sum of digits of the number nums[i] is equal to that of nums[j].

# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

from collections import defaultdict
import heapq

class Solution:
    def maximumSum(self, nums) -> int:
        def add_digs(num):
            res = 0
            s = str(num)
            for i in range(len(s)):
                res += int(s[i])
            return res
        
        digs = []
        for char in nums:
            digs.append(add_digs(char))

        res = -1
        
        left = defaultdict(list)

        for i in range(len(digs)):
            left[digs[i]].append(i)

        for j in left:
            arr = left[j]
            if len(arr) == 1:
                continue
            ma = []
            heapq.heapify(ma)
            for i in arr:
                heapq.heappush(ma, -1 * nums[i])
            bigone = heapq.heappop(ma)
            bigtwo = heapq.heappop(ma)
            queue = -bigone + -bigtwo
            res = max(res, queue)
        return res

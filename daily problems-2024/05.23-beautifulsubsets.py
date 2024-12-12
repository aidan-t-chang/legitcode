# You are given an array nums of positive integers and a positive integer k.

# A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

# Return the number of non-empty beautiful subsets of the array nums.

# A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

import collections

class Solution:
    def beautiful(self, nums, k):
        def dfs(idx):
            if idx == len(nums):
                self.count += 1
                return 

            # take index
            # take num = nums[idx] only if subset does not have x - k or x + k
            num = nums[idx]
            if bad[num] == 0:
                bad[num + k] += 1
                bad[num - k] += 1
                dfs(idx + 1)
                bad[num + k] -= 1
                bad[num - k] -= 1
            # dont take index
            dfs(idx + 1)            
        bad = collections.defaultdict(int)
        self.count = 0
        dfs(0)
        return self.count - 1 # - 1 to remove the empty subset
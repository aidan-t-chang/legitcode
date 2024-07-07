# You are given an array of distinct integers nums and a target integer target. 
# Your task is to return a list of all unique combinations of nums 
# where the chosen numbers sum to target.

# The same number may be chosen from nums an unlimited number of times. 
# Two combinations are the same if the frequency of each of the chosen numbers
# is the same, otherwise they are different.

# You may return the combinations in any order and 
# the order of the numbers in each combination can be in any order.


class Solution:
    def combinationSum(self, nums, target):
        res = []

        def dfs(i, cur, total): # cur = current combination
            if total == target:
                res.append(cur.copy()) # going to keep using cur, so have to create a copy of the variable
                return
            elif i >= len(nums) or total > target:
                return
            
            cur.append(nums[i]) # choose to include this value
            dfs(i, cur, total + nums[i]) # left side of the decision tree (choosing the value)

            cur.pop()
            dfs(i+1, cur, total) # right side of the decision tree (not choosing the value)
        
        dfs(0, [], 0)
        return res
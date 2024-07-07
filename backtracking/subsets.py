# Given an array nums of unique integers, 
# return all possible subsets of nums.

# The solution set must not contain duplicate subsets. 
# You may return the solution in any order.

class Solution:
    def subsets(self, nums):
        res = []

        subset = [] 
        def dfs(i): # index of the value we are making the decision on
            if i >= len(nums): # if the index is out of bounds
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1) # left branch of the decision tree
            
            #each recursive call will have a different subset:
            # one with the new subset val and one without
            #decision to not include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
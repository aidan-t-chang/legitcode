# Given an integer array nums that may contain duplicates, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums): # have gone through the entire array
                res.append(subset.copy())
                return
            
            #all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            #all subsets that do not include nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]: # if the next value in nums is the same as the current one:
                # (one subtree will never have the same number as the other)
                i += 1
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return res



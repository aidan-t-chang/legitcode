# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and 
# return the number of different non-empty subsets with the maximum bitwise OR.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) 
# elements of b. Two subsets are considered different if the indices of the elements chosen are different.

# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

class Solution:
    def backtrack(self, nums, index, currentOR, maxOR, count):
        if currentOR == maxOR:
            count[0] += 1
        
        for i in range(index, len(nums)):
            self.backtrack(nums, i + 1, currentOR | nums[i], maxOR, count)
    
    def countMaxOrSubsets(self, nums):
        maxOR = 0
        
        # Step 1: Compute the maximum OR
        for num in nums:
            maxOR |= num
        
        count = [0]
        # Step 2: Backtrack to count the subsets
        self.backtrack(nums, 0, 0, maxOR, count)
        
        return count[0]
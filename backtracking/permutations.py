# Given an array nums of distinct integers, 
# return all the possible permutations. 
# You can return the answer in any order.


class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        
        res = []
        subproblem = self.permute(nums[1:]) # remove the first value to insert everywhere
        for num in subproblem:
            for i in range(len(num)+1):
                copy = num.copy()
                copy.insert(i, nums[0]) # insert the removed value in all possible places for all possible permutations
                res.append(copy)
        return res
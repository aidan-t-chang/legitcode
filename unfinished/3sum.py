# Given an integer array nums, 
# return all the triplets [nums[i], nums[j], nums[k]] such that 
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threesum(nums):
    i = 0
    k = len(nums) - 1
    
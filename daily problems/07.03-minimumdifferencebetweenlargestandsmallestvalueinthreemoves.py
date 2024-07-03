# You are given an integer array nums.

# In one move, 
# you can choose one element of nums and change it to any value.

# Return the minimum difference between the 
# largest and smallest value of nums after performing at most three moves.

from collections import Counter

def mana(nums):
    if len(nums) <= 4:
        return 0
    nums.sort()
    res = nums[-1] - nums[0]
    for i in range(4):
        res = min(res, nums[-(4-i)] - nums[i])
    return res

mana([1,5,0,10,14,1,1,1])
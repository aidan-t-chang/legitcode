# Given an integer array nums, 
# return all the triplets [nums[i], nums[j], nums[k]] such that 
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threesum(nums):
    res = []
    nums.sort()

    for i, v in enumerate(nums): # for every index and value in nums
        # if the number is not the first (i > 0) and it's the same number as the one before it
        if i > 0 and v == nums[i-1]:
            continue

        L, R = i+1, len(nums) - 1
        while L < R: # two sum 2
            three = v + nums[L] + nums[R]
            if three > 0:
                R -= 1
            elif three < 0:
                L += 1
            else:
                res.append([v, nums[L], nums[R]])
                L += 1
                while nums[L] == nums[L-1] and L < R:
                    # if they are the same value, we need to change the value still
                    L += 1

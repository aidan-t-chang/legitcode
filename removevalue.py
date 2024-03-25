# Given an integer array nums and an integer val, 
# remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
# same as removeduplicates.py, leetcode asks for stupid return value.
# im not following that. realsolution() is the real solution though

def removeElement(nums, val):
    vale = []
    for c in nums:
        if c != val:
            vale.append(c)
    nums = vale
    return nums

def realsolution(self, nums, val):
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

(print(removeElement([3,2,2,3], 3)))
(print(removeElement([0,1,2,2,3,0,4,2], 2)))
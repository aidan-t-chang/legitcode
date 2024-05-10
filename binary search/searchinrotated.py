# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, 
# nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, 

# return the index of target if it is in nums, or -1 if it is not in nums.

def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] >= nums[l]: # left portion
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target < nums[r]:
                r = mid - 1
            else: # target greater than middle value and target < right value, we only search right portion
                l = mid + 1
    return -1
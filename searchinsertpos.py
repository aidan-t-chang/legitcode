# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.


# binary search must use!!
def searchInsert(nums, target):
    min = 0
    max = len(nums) - 1
    avg = (min + max) // 2
    if target in nums:
        while True:
            if nums[avg] == target:
                return avg
            if nums[avg] < target:
                min = avg + 1
                avg = (min + max) // 2
            if nums[avg] > target:
                max = avg - 1
                avg = (min + max) // 2
    while True:
        if nums[0] >= target:
            return 0
        if nums[max - 1] <= target:
            return len(nums)
        if nums[avg - 1] < target < nums[avg] + 1:
            return avg
        if nums[avg] < target:
            min = avg + 1
            avg = (min + max) // 2
        if nums[avg] > target:
            max = avg - 1
            avg = (min + max) // 2

def binary2(nums, target):
    min = 0
    max = len(nums) - 1
    avg = (min + max) // 2
    return nums

print('return 4', searchInsert([1,3,5,6], 7))
print('return 1', searchInsert([1,3,5,6], 2))
print('return 2', searchInsert([1,3,5,6], 5))
print('return 0', searchInsert([1,3,5,6], 0))
print('return 1', searchInsert([1,3], 2))
print('return 2', searchInsert([1,4,6,7,8,9], 6))
print('return 2', searchInsert([1,2,4,5,6], 3))
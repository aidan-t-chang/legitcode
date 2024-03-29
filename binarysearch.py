# write a binary search.

def binarySearch(nums, target):
    min = 0
    max = len(nums)
    mid = (min + max) // 2
    while True:
        if target not in nums:
            return -1
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            min = mid + 1
            mid = (min + max) // 2
        else:
            max = mid - 1
            mid = (min + max) // 2
    return mid
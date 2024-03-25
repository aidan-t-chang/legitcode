def binarySearch(nums, target):
    min = 0
    max = len(nums)
    avg = (min + max) // 2
    while True:
        if nums[avg] == target:
            return avg
        if nums[avg] < target:
            min = avg + 1
            avg = (min + max) // 2
        else:
            max = avg - 1
            avg = (min + max) // 2
    return avg
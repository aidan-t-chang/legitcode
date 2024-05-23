# stupid question, remover 4 and 5 work but remover 5 returns and
# does what leetcode wants you to do
# Question: Remove duplicate numbers from a sorted array
# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element 
# appears only once. The relative order of the elements should be 
# kept the same. Then return the number of unique elements in nums.

def remover(nums):
    arr = []
    for i in range(0, len(nums)):
        if i+1 < len(nums):
            if nums[i] == nums[i+1]:
                nums.pop(nums[i])
                arr.append(nums[i])
            else:
                arr.append(nums[i])
        if i == len(nums) - 1:
            arr.append(nums[i])
    return len(arr), arr


def remover2(nums):
    for i in range(0, len(nums)):
        if i+1 < len(nums) and nums[i] == nums[i+1]:
            nums.pop(nums[i])
            print(nums)
    return len(nums), nums

def remover3(nums):
    cc = []
    c = 0
    while c < len(nums) - 1:
        if nums[c] != nums[c+1]:
            cc.append(nums[c])
            c += 1
        else:
            c += 1
    cc.append(nums[-1])
    k = len(cc)
    nums = cc
    return k, cc

def remover4(nums):
    c = 0
    while c < len(nums) - 1:
        if nums[c] == nums[c+1]:
            nums.pop(c)
            c += 1
        else:
            c += 1
    k = len(nums)
    return nums

def remover5(nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

print(remover4([1,1,2]))
print(remover4([1,1,2,3,4,5,5]))
print(remover4([1,1,2,3,3,4,5,5]))
print(remover4([0,0,1,1,1,2,2,3,3,4]))

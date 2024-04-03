# Given an integer array nums, 
# return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains(nums):
    n = sorted(nums)
    for i in range(len(n) - 1):
        if n[i] == n[i+1]:
            return True
    return False

print(contains([1,2,3,1]))
print(contains([1,2,4,3,4]))

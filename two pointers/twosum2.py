# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, 
# index1 and index2, added by one as an integer array [index1, index2] of length 2.

def twosum2(numbers, target):
    L = 0
    R = len(numbers) - 1
    while L < R:
        sum = numbers[L] + numbers[R]
        if sum == target:
            return [L+1, R+1]
        if sum < target: 
            L += 1
        else:
            R -= 1
    
print(twosum2([2,7,11,15], 9))
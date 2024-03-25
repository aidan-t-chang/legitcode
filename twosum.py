# Given an array of integers (nums) and an integer (target), 
# return indices of the two numbers such that they add up to target.

def twosum(nums, target):
    pair = []
    c1 = 0
    c2 = 1
    c3 = 1
    stopper = False
    if nums[0] + nums[1] == target:
        pair = [0,1]

    while stopper == False:
        if nums[c1] + nums[c2] == target:
            pair = [c1, c2]
            stopper = True
        if c2 == len(nums) - 1:
            c2 = c3
            c1 = c2 - 1
            c3 += 1    
        else:
            c2 += 1
    return pair


print(twosum([5,6,2,12,13,14,17], 26))

print('running')

# Given an integer array nums, 
# # return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):
    ret = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        ret[i] = prefix # take the prefix and put it in that position in the output array (ret)
        prefix *= nums[i] # update the prefix as the iteration goes through nums
    postfix = 1
    for i in range(len(nums) - 1, -1, -1): # start at the end of the input array and go up until the beginning
        ret[i] *= postfix # not storing the postfix but multiplying the value that is already in the output array, since all values are already updated by the prefix in ret
        postfix *= nums[i]
    return ret

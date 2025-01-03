# You are given a 0-indexed integer array nums of length n.

# nums contains a valid split at index i if the following are true:

# The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
# There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.

class Solution:
    def waysToSplitArray(self, nums) -> int:
        psum = [0]
        for n in nums:
            psum.append(psum[-1]+n)
        psum = psum[1:]

        res = 0
        for i in range(len(nums)-1):
            last_elements = psum[-1] - psum[i]
            print(last_elements, psum[i])
            if psum[i] >= last_elements:
                res += 1
 
        return res
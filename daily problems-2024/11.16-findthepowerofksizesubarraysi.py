# You are given an array of integers nums of length n and a positive integer k.

# The power of an array is defined as:

# Its maximum element if all of its elements are consecutive and sorted in ascending order.
# -1 otherwise.
# You need to find the power of all 
# subarrays
#  of nums of size k.

# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].


class Solution:
    def resultsArray(self, nums, k: int):
        res = []

        l = 0
        for r in range(k-1, len(nums)):
            temp = sorted(nums[l:r+1])
            if temp == nums[l:r+1] and nums[l:r+1] == [i for i in range(temp[0], temp[0] + k)]:
                res.append(max(nums[l:r+1]))
            else:
                res.append(-1)
            l += 1
        return res
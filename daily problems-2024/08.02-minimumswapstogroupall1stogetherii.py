# A swap is defined as taking two distinct positions in an array and swapping the values in them.

# A circular array is defined as an array where we consider the first element and the last element to be adjacent.

# Given a binary circular array nums, return the minimum number of swaps required to group all 1's 
# present in the array together at any location.


class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        c = nums.count(1)
        l = 0
        window_ones = max_window_ones = 0
        for r in range(2*n):
            if nums[r % n]:
                window_ones += 1
            if r - l + 1 > c:
                window_ones -= nums[l % n]
                l += 1
            max_window_ones = max(max_window_ones, window_ones)
        return c - max_window_ones               
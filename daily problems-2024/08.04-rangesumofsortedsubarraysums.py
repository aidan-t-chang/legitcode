# You are given the array nums consisting of n positive integers. 
# You computed the sum of all non-empty continuous subarrays from the array and then sorted them in 
# non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

# Return the sum of the numbers from index left to index right (indexed from 1), 
# inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

class Solution:
    def rangeSum(self, nums, n: int, left: int, right: int) -> int:
        arr = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                arr.append(s)
        arr.sort()
        mod = 10**9 + 7
        return sum(arr[left - 1 : right]) % mod
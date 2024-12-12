# You are given an array nums of non-negative integers and an integer k.

# An array is called special if the bitwise OR of all of its elements is at least k.

# Return the length of the shortest special non-empty 
# subarray
#  of nums, or return -1 if no special subarray exists.

class Solution:
    def minimumSubarrayLength(self, nums, k: int) -> int:
        def update(bits, n, diff):
            for i in range(32):
                if n & (1 << i):
                    bits[i] += diff

        def bits_to_int(bits):
            res = 0
            for i in range(32):
                if bits[i]:
                    res += (1 << i)
            return res

        res = float('inf')
        bits = [0] * 32
        l = 0
        for r in range(len(nums)):
            update(bits, nums[r], 1)
            cur_or = bits_to_int(bits)

            while cur_or >= k and l <= r:
                res = min(res, r - l + 1)
                update(bits, nums[l], -1)
                cur_or = bits_to_int(bits)
                l += 1

        return -1 if res == float('inf') else res
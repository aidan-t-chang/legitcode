# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

class Solution:
    def tupleSameProduct(self, nums) -> int:
        pair_products = []

        num_tupes = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                pair_products.append(nums[i] * nums[j])

        pair_products.sort()

        last_seen = -1
        same = 0

        for i in range(len(pair_products)):
            if pair_products[i] == last_seen:
                same += 1
            else:
                pairs = same * (same - 1) // 2
                num_tupes += 8 * pairs
                last_seen = pair_products[i]
                same = 1
        
        equal = same * (same - 1) // 2
        num_tupes += 8 * equal
        return num_tupes
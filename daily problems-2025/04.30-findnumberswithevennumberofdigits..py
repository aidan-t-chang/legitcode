""" Given an array nums of integers, return how many of them contain an even number of digits. """

class Solution:
    def findNumbers(self, nums) -> int:
        count = 0
        for n in nums:
            count += 0 if len(str(n)) % 2 else 1
        return count
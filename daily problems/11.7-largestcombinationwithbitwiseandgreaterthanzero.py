# The bitwise AND of an array nums is the bitwise AND of all integers in nums.

# For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
# Also, for nums = [7], the bitwise AND is 7.
# You are given an array of positive integers candidates. Evaluate the bitwise 
# AND of every combination of numbers of candidates. Each number in candidates may 
# only be used once in each combination.

# Return the size of the largest combination of candidates with a bitwise AND greater than 0.


class Solution:
    def largestCombination(self, candidates) -> int:
        res = [0] * 32

        for candidate in candidates:
            i = 31
            while candidate > 0:
                an = candidate & 1

                res[i] += an

                candidate >>= 1
                i -= 1

        return max(res)

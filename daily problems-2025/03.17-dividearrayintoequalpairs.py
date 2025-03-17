# You are given an integer array nums consisting of 2 * n integers.

# You need to divide nums into n pairs such that:

# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.
from collections import Counter
class Solution:
    def divideArray(self, nums) -> bool:
        count = Counter(nums)
        for c in count:
            if count[c] % 2:
                return False

        return True
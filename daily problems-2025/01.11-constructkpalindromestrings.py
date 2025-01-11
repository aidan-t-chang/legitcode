# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.
from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False

        count = Counter(s)

        count_odd = 0
        for c in count:
            if count[c] % 2:
                count_odd += 1

        return not (count_odd > k)
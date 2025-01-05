# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with 
# some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".

from collections import Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)


        for mid in s:
            right[mid] -= 1

            for c in left:
                if right[c] > 0:
                    res.add((mid, c)) # could possibly be a duplicate
            left.add(mid)
        return len(res)

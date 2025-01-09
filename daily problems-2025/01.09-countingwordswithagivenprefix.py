# You are given an array of strings words and a string pref.

# Return the number of strings in words that contain pref as a prefix.

# A prefix of a string s is any leading contiguous substring of s.


class Solution:
    def prefixCount(self, words, pref: str) -> int:
        res = 0
        for word in words:
            if word[:len(pref)] == pref:
                res += 1
        return res
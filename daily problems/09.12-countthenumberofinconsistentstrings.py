# You are given a string allowed consisting of distinct characters and an array of strings words. 
# A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.


class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        res = 0

        allow = [s for s in allowed]

        for word in words:
            if all(char in allow for char in word):
                res += 1
        return res
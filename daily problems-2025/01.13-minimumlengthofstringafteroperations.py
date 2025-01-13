# You are given a string s.

# You can perform the following process on s any number of times:

# Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
# Delete the closest character to the left of index i that is equal to s[i].
# Delete the closest character to the right of index i that is equal to s[i].
# Return the minimum length of the final string s that you can achieve.
from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)

        for f in freq:
            while freq[f] >= 3:
                freq[f] -= 2
        
        res = 0
        for count in freq.values():
            res += count

        return res
# You are given a 0-indexed binary string s having an even length.

# A string is beautiful if it's possible to partition it into one or more substrings such that:

# Each substring has an even length.
# Each substring contains only 1's or only 0's.
# You can change any character in s to 0 or 1.

# Return the minimum number of changes required to make the string s beautiful.


class Solution:
    def minChanges(self, s: str) -> int:
        
        #just go through s in a sliding window of fixed size 2 and count # of different bits?


        l, r = 0, 1
        count = 0

        while r < len(s):
            if s[l] != s[r]:
                count += 1
            l += 2
            r += 2
        
        return count
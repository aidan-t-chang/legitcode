# Given a string s of zeros and ones, return the maximum score after splitting the string into 
# two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the 
# number of ones in the right substring.


class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeroes = m = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeroes += 1
            else:
                ones -= 1
            m = max(m, zeroes + ones)

        return m
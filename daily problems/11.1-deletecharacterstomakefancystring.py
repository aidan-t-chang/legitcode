# A fancy string is a string where no three consecutive characters are equal.

# Given a string s, delete the minimum possible number of characters from s to make it fancy.

# Return the final string after the deletion. It can be shown that the answer will always be unique.


class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        count = 1

        res += s[0]

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            if count < 3:
                res += s[i]

        return res
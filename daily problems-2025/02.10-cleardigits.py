# You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

class Solution:
    def clearDigits(self, s: str) -> str:
        mark = [0] * len(s)
        for i in range(len(s)):
            if s[i].isnumeric():
                mark[i] = 1
                for j in range(i,-1,-1):
                    if not s[j].isnumeric() and not mark[j]:
                        mark[j] = 1
                        break

        res = ""
        for i in range(len(s)):
            if not mark[i]:
                res += s[i]
        return res
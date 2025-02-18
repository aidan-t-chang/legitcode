# You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

# A 0-indexed string num of length n + 1 is created using the following conditions:

# num consists of the digits '1' to '9', where each digit is used at most once.
# If pattern[i] == 'I', then num[i] < num[i + 1].
# If pattern[i] == 'D', then num[i] > num[i + 1].
# Return the lexicographically smallest possible string num that meets the conditions.

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.res = []

        self.build(0, 0, pattern)

        return "".join(self.res[::-1])

    def build(self, i, cur, pattern):
        if i != len(pattern):
            if pattern[i] == "I":
                self.build(i+1, i+1, pattern)
            else:
                cur = self.build(i+1, cur, pattern)
        self.res.append(str(cur+1))

        return cur + 1
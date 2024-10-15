# There are n balls on a table, each ball has a color black or white.

# You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.

# In each step, you can choose two adjacent balls and swap them.

# Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.

class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        blacks = 0

        for char in s:
            if char == '0':
                res += blacks
            else:
                blacks += 1

        return res


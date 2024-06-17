# Given a non-negative integer c, determine whether
# there are two integers a and b such that
# a^2 + b^2 = c.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = math.floor(sqrt(c))

        while l <= r:
            potential = l**2 + r**2
            if potential == c:
                return True
            elif potential > c:
                r -= 1
            else:
                l += 1
        return False
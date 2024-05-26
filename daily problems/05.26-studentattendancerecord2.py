# An attendance record for a student can be represented as a string where each 
# character signifies whether the student was absent, late, or present on that day. 
# The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, 
# return the number of possible attendance records of length n that make a student eligible for an attendance award. 
# The answer may be very large, so return it modulo 109 + 7
from collections import defaultdict


class Solution:
    def checkRecord(self, n):
        mod = 10**9 + 7


        if n == 1:
            return 3
        tem = {
                    (0, 0): 1, (0, 1): 1, (0, 2): 0,
                    (1, 0): 1, (1, 1): 0, (1, 2): 0
                }

        for i in range(n - 1):
            res = defaultdict(int)

            #choose p
            res[(0, 0)] = ((tem[(0,0)] + tem[(0, 1)]) % mod + tem[(0, 2)]) % mod
            res[(1, 0)] = ((tem[(1,0)] + tem[(1, 1)]) % mod + tem[(1, 2)]) % mod
            #choose l
            res[(0, 1)] = tem[(0,0)]
            res[(1, 1)] = tem[(1,0)]
            res[(0, 2)] = tem[(0,1)]
            res[(1, 2)] = tem[(1,1)]
            #choose a
            res[(1,0)] = (res[(1,0)] + (((tem[(0, 0)] + tem[(0, 1)]) % mod + tem[(0, 2)])) % mod) % mod
            tem = res

        return sum(tem.values()) % mod
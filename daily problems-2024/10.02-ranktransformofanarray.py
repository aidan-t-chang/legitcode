# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.
from collections import defaultdict

class Solution:
    def arrayRankTransform(self, arr):
        welcome = list(set(arr.copy()))
        welcome.sort()
        has = defaultdict(int)

        i = 1
        for val in welcome:
            has[val] = i
            i += 1

        res = []
        for val in arr:
            res.append(has[val])
        return res
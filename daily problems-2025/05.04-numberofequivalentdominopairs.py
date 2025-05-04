""" Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j]. """
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        seen = defaultdict(int)
        res = 0
        for a, b in dominoes:
            if a == b:
                res += seen[(a, b)]
            else:
                res += seen[(a, b)]
                res += seen[(b, a)]
            seen[(a, b)] += 1
        return res
# A sentence is a string of single-space separated words where each word 
# consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, 
# and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. 
# You may return the answer in any order.
from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        s1 = s1.split()
        s2 = s2.split()

        counts = defaultdict(int)

        for s in s1:
                counts[s] += 1

        for s in s2:
                counts[s] += 1

        res = []
        for c in counts:
            if counts[c] == 1:
                res.append(c)
        return res



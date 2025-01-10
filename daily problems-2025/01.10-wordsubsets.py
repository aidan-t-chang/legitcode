# You are given two string arrays words1 and words2.

# A string b is a subset of string a if every letter in b occurs in a including multiplicity.

# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.

# Return an array of all the universal strings in words1. You may return the answer in any order.
from collections import defaultdict


class Solution:
    def wordSubsets(self, words1, words2):
        w2_freq = defaultdict(int)

        res = []
        for word in words2:
            temp = defaultdict(int)
            for letter in word:
                temp[letter] += 1
            for key in temp:
                w2_freq[key] = max(w2_freq[key], temp[key])

        for word in words1:
            count = defaultdict(int)
            for letter in word:
                count[letter] += 1
            if all(count[key] >= w2_freq[key] for key in w2_freq):
                res.append(word)
        return res
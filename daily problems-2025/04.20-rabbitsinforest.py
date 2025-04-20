""" There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest. """
from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers) -> int:
        count = Counter(answers)

        total = 0
        for c in count:
            total += ceil(float(count[c]) / (c + 1)) * (c + 1)
        return int(total)
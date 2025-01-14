# You are given two 0-indexed integer permutations A and B of length n.

# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

# Return the prefix common array of A and B.

# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
from collections import defaultdict

class Solution:
    def findThePrefixCommonArray(self, A, B):
        freq = defaultdict(int)
        
        c = [0]
        for i in range(len(A)):
            temp = 0
            freq[A[i]] += 1
            freq[B[i]] += 1
            if A[i] != B[i]:
                if freq[A[i]] == 2:
                    temp += 1
                if freq[B[i]] == 2:
                    temp += 1
            else:
                temp += 1
            c.append(c[-1] + temp)

        return c[1:]
            

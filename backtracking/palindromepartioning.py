# Given a string s, partition s such that every substring
# of the partition is a palindrome. 
# Return all possible palindrome partitioning of s.

class Solution:
    def partition(self, s: str):
        res = []
        partition = []

        def backtrack(i):
            if i >= len(s): # every single index value has been visited
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)): # go through the remaining values that must be checked
                if self.par(s, i, j):
                    partition.append(s[i:j+1]) # valid palindromic substring
                    backtrack(j+1)
                    partition.pop()
        backtrack(0)
        return res

    def par(self, s, l, r):

        while l <= r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True
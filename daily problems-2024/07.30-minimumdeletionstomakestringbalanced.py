# You are given a string s consisting only of characters 'a' and 'b'​​​​.

# You can delete any number of characters in s to make s balanced. 
# s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

# Return the minimum number of deletions needed to make s balanced.


class Solution:
    def minimumDeletions(self, s):
        a = [0] * len(s)
        for i in range(len(s)-2, -1, -1):
            a[i] = a[i+1]
            a[i] += 1 if s[i+1] == 'a' else 0
        
        b = 0
        res = len(s)

        for i, c in enumerate(s):
            res = min(res, b + a[i])
            if c == "b":
                b += 1
        return res
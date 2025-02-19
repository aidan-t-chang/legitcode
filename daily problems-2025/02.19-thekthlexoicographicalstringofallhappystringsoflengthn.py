# A happy string is a string that:

# consists only of letters of the set ['a', 'b', 'c'].
# s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

# Return the kth string of this list or return an empty string if there are less than k happy strings of length n

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def backtrack(cur):
            if len(cur) == n:
                copy = cur.copy()
                res.append("".join(copy))
                return
            
            for char in ['a', 'b', 'c']:
                if len(cur) > 0 and cur[-1] == char:
                    continue
                
                cur.append(char)
                backtrack(cur)
                cur.pop()

        backtrack([])
        
        if k > len(res):
            return ""
        res.sort()
        return res[k-1]
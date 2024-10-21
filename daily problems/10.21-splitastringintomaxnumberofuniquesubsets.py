# Given a string s, return the maximum number of unique substrings that the given string can be split into.

# You can split string s into any list of non-empty substrings, where the concatenation of the 
# substrings forms the original string. However, you must split the substrings such that all of them are unique.

# A substring is a contiguous sequence of characters within a string.


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def dfs(i, cur):
            if i == len(s):
                return 0
            
            res = 0
            for j in range(i, len(s)):
                substring = s[i:j+1]

                if substring not in cur:
                    cur.add(substring)
                    res = max(res, 1 + dfs(j+1, cur))
                    cur.remove(substring)
            return res
        
        return dfs(0, set())
        

        
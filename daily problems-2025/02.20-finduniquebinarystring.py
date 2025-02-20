# Given an array of strings nums containing n unique binary strings each of length n, 
# return a binary string of length n that does not appear in nums. 
# If there are multiple answers, you may return any of them.

class Solution:
    def findDifferentBinaryString(self, nums) -> str:
        res = []
        n = len(nums)

        def dfs(cur):
            if len(cur) == n:
                if cur not in nums:
                    res.append(cur)
                return
            
            dfs(cur + "0")
            dfs(cur + "1")

        dfs("")
        return res[-1]
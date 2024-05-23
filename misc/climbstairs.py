# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# solution uses fibonacci numbers (1,2,3,5,8, etc.)
# however, writing this using recursion uses too much memory,
# so memoization is used instead.

class Solution:
    def climbStairs(self, n):
        memo = {}
        return self.help(n, memo)
    
    def help(self, n, memo):
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.help(n-1, memo) + self.help(n-2, memo)
        return memo[n]
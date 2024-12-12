# Alice and Bob continue their games with piles of stones.  
# There are a number of piles arranged in a row, and each pile has a 
# positive integer number of stones piles[i].  
# The objective of the game is to end with the most stones. 

# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

# On each player's turn, that player can take all the stones in the first X 
# remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

# The game continues until all the stones have been taken.

# Assuming Alice and Bob play optimally, return the maximum number of 
# stones Alice can get.

class Solution:
    def stoneGameII(self, piles) -> int:
        dp = {}

        #returns the number of stones alice gets
        def dfs(alice, i, M):
            if i == len(piles):
                return 0 
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]

            res = 0 if alice else float('inf')
            total = 0
            for X in range(1, 2 * M + 1): # non inclusive
                if i + X > len(piles):
                    break
                total += piles[i + X - 1] # - 1 because X starts at one
                if alice:
                    res = max(res, total + dfs(not alice, i + X, max(M, X)))
                else:
                    res = min(res, dfs(not alice, i + X, max(M, X)))
            dp[(alice, i, M)] = res
            return res
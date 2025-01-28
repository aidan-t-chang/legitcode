# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

# A land cell if grid[r][c] = 0, or
# A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations any number of times:

# Catch all the fish at cell (r, c), or
# Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.


class Solution:
    def findMaxFish(self, grid) -> int:
        su = []
        row, col = len(grid), len(grid[0])
        
        def dfs(r, c, cur, visit):
            if r < 0 or c < 0 or r == row or c == col:
                su.append(cur.copy())
                return
            if (r, c) in visit:
                return
            if grid[r][c] == 0:
                su.append(cur.copy())
                return
            visit.add((r, c))
            cur.append(grid[r][c])
            dfs(r+1, c, cur, visit)
            dfs(r-1, c, cur, visit)
            dfs(r, c+1, cur, visit)
            dfs(r, c-1, cur, visit)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] != 0:
                    dfs(r, c, [], set())

        res = 0
        for perm in su:
            res = max(res, sum(perm))
        return res
# You are given a 0-indexed m x n matrix grid consisting of positive integers.

# You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

# From a cell (row, col), you can move to any of the cells: 
# (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, 
# should be strictly bigger than the value of the current cell.
# Return the maximum number of moves that you can perform.

class Solution:
    def maxMoves(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            moves = 0
            for r, c in [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]:
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] > grid[row][col]:
                    moves = max(moves, 1 + dfs(r, c))
            memo[(row, col)] = moves
            return moves
        
        memo = {}
        max_moves = 0
        for row in range(rows):
            max_moves = max(max_moves, dfs(row, 0))
        
        return max_moves
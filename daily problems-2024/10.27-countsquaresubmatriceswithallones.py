# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

class Solution:
    def countSquares(self, matrix) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r, c):
            if r == rows or c == cols or not matrix[r][c]:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]


            # length of the maximum current square
            memo[(r, c)] = 1 + min(dfs(r+1, c), dfs(r, c+1), dfs(r+1, c+1))
            return memo[(r, c)]

        res = 0
        for r in range(rows):
            for c in range(cols):
                res += dfs(r, c)
        return res
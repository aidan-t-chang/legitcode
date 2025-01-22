# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

# If isWater[i][j] == 0, cell (i, j) is a land cell.
# If isWater[i][j] == 1, cell (i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:

# The height of each cell must be non-negative.
# If the cell is a water cell, its height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. 
# A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter 
# (i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.

# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. 
# If there are multiple solutions, return any of them.
from collections import deque


class Solution:
    def highestPeak(self, isWater):
        row, col = len(isWater), len(isWater[0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        grid = [[-1 for _ in range(col)] for _ in range(row)]

        q = deque()
        for r in range(row):
            for c in range(col):
                if isWater[r][c]:
                    q.append((r, c))
                    grid[r][c] = 0

        cur_layer = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                for d in range(4):
                    nx = cur[0] + dx[d]
                    ny = cur[1] + dy[d]

                    if nx >= 0 and nx < row and ny >= 0 and ny < col and grid[nx][ny] == -1:
                        grid[nx][ny] = cur_layer
                        q.append((nx, ny))
            cur_layer += 1
        return grid
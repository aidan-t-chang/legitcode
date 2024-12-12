# You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), 
# which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].

# You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. 
# Each move you make takes 1 second.

# Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.

import heapq

class Solution:
    def minimumTime(self, grid) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1

        min_heap = [(0, 0, 0)] # (time, row, col)

        rows, cols = len(grid), len(grid[0])
        visit = set()

        while min_heap:
            t, r, c =heapq.heappop(min_heap)

            if (r, c) == (rows - 1, cols - 1):
                return t

            neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in neighbors:
                wait = 0
                if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in visit:
                    continue
                if abs(grid[nr][nc] - t) % 2 == 0:
                    wait = 1

                next_time = max(t + 1, grid[nr][nc] + wait)
                heapq.heappush(min_heap, (next_time, nr, nc))
                visit.add((nr, nc))
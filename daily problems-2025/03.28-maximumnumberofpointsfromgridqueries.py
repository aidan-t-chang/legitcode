# You are given an m x n integer matrix grid and an array queries of size k.

# Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

# If queries[i] is strictly greater than the value of the current cell that you are in, 
# then you get one point if it is your first time visiting this cell, 
# and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
# Otherwise, you do not get any points, and you end this process.
# After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

# Return the resulting array answer.
import heapq
class Solution(object):
    def valid(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m

    def maxPoints(self, grid, queries):
        n, m = len(grid), len(grid[0])
        res = [0] * len(queries)
        q = sorted((queries[i], i) for i in range(len(queries)))
        visited = [[-1] * m for _ in range(n)]
        minh = [(grid[0][0], 0, 0)]
        visited[0][0] = 1
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        count = 0

        for val, idx in q:
            while minh and minh[0][0] < val:
                count += 1
                _, x, y = heapq.heappop(minh)
                for j in range(4):
                    newx, newy = x + dx[j], y + dy[j]
                    if self.valid(newx, newy, n, m) and visited[newx][newy] == -1:
                        visited[newx][newy] = 1
                        heapq.heappush(minh, (grid[newx][newy], newx, newy))
            res[idx] = count

        return res
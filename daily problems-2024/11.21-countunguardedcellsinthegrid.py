# You are given two integers m and n representing a 0-indexed m x n grid. 
# You are also given two 2D integer arrays guards and walls where 
# guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the 
# positions of the ith guard and jth wall respectively.

# A guard can see every cell in the four cardinal directions 
# (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. 
# A cell is guarded if there is at least one guard that can see it.

# Return the number of unoccupied cells that are not guarded.

class Solution:
    def countUnguarded(self, m: int, n: int, guards, walls) -> int:
        grid = [[0] * n for _ in range(m)]
        # 0 is free, 1 is guard, 2 wall, 3 guardable position

        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        def mark_guarded(r, c):
            for row in range(r+1, m):
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3
            for row in reversed(range(0, r)):
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3
            for col in range(c+1, n):
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3

            for col in reversed(range(0, c)):
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3

        for r, c in guards:
            mark_guarded(r, c)

        res = 0
        for row in grid:
            for n in row:
                if n == 0:
                    res += 1


        return res
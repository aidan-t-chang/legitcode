# You are given an m x n binary grid grid where 1 represents land and 0 represents water. 
# An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

# In one day, we are allowed to change any single land cell (1) into a water cell (0).

# Return the minimum number of days to disconnect the grid.


class Solution:
    # Directions for adjacent cells: right, left, down, up
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minDays(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # Count initial islands
        initial_island_count = self._count_islands(grid)
        # Already disconnected or no land
        if initial_island_count != 1:
            return 0
        # Try removing each land cell
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue  # Skip water
                # Temporarily change to water
                grid[row][col] = 0
                new_island_count = self._count_islands(grid)
                # Check if disconnected
                if new_island_count != 1:
                    return 1
                # Revert change
                grid[row][col] = 1
        return 2

    def _count_islands(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        island_count = 0
        # Iterate through all cells
        for row in range(rows):
            for col in range(cols):
                # Found new island
                if not visited[row][col] and grid[row][col] == 1:
                    self._explore_island(grid, row, col, visited)
                    island_count += 1
        return island_count

    def _explore_island(
        self,
        grid: List[List[int]],
        row: int,
        col: int,
        visited: List[List[bool]],
    ) -> None:
        visited[row][col] = True
        # Check all adjacent cells
        for direction in self.DIRECTIONS:
            new_row = row + direction[0]
            new_col = col + direction[1]
            # Explore if valid land cell
            if self._is_valid_land_cell(grid, new_row, new_col, visited):
                self._explore_island(grid, new_row, new_col, visited)

    def _is_valid_land_cell(
        self,
        grid: List[List[int]],
        row: int,
        col: int,
        visited: List[List[bool]],
    ) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        # Check bounds, land, and not visited
        return (
            0 <= row < rows
            and 0 <= col < cols
            and grid[row][col] == 1
            and not visited[row][col]
        )
        
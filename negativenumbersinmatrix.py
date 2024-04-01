# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
# return the number of negative numbers in grid.

def countNegatives(grid):
    c = 0
    rows,columns = len(grid), len(grid[0])
    index = columns - 1

    for row in range(rows):
        while index >= 0 and grid[row][index] < 0:
            index -= 1
        c += index + 1
    return (rows * columns) - c


print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
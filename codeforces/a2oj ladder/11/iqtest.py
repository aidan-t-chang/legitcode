def solve():
    grid = []
    for i in range(4):
        line = input()
        grid.append(line)
    # print(grid)
    
    for row in range(3):
        for col in range(3):
            pcount = 0
            pcount += (grid[row][col] == ".")
            pcount += (grid[row][col+1] == ".")
            pcount += (grid[row+1][col] == ".")
            pcount += (grid[row+1][col+1] == ".")
            if pcount <= 1 or pcount >= 3:
                return "YES"
            
    return "NO"
            
            
print(solve())

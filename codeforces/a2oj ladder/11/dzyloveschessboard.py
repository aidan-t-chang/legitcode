row, col = map(int, input().split())

grid = []
for i in range(row):
    inp = input()
    arr = [inp[i] for i in range(len(inp))]
    grid.append(arr)

# def dfs(r, c, prev):
#     if r == row or c == col:
#         return
#     if grid[r][c] == ".":
#         if prev == "W":
#             grid[r][c] = "B"
#             dfs(r+1, c, "B")
#             dfs(r, c+1, "B")
#             dfs(r+1, c+1, "B")
#         else:
#             grid[r][c] = "W"
#             dfs(r+1, c, "W")
#             dfs(r, c+1, "W")
#             dfs(r+1, c+1, "W")
#     else:
#             dfs(r+1, c, prev)
#             dfs(r, c+1, prev)
#             dfs(r+1, c+1, prev)
            
def solve():
    for r in range(row):
        for c in range(col):
            if grid[r][c] == ".":
                if not r % 2:
                    if c % 2:
                        grid[r][c] = "W"
                    else:
                        grid[r][c] = "B"
                else:
                    if c % 2:
                        grid[r][c] = "B"
                    else:
                        grid[r][c] = "W"

solve()
for row in grid:
    print("".join(row))
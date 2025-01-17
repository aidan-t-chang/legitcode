grid = []
for _ in range(8):
    grid.append(input())

row = col = 8

rows = set()
posd = set()
negd = set()

res = []
def backtrack(c):
    if c == 8:
        res.append(0)
        return
    for r in range(row):
        if r in rows or (r + c) in posd or (r - c + 7) in negd or grid[r][c] == "*":
            continue
        rows.add(r)
        posd.add(r+c)
        negd.add(r-c+7)
        backtrack(c+1)
        rows.remove(r)
        posd.remove(r+c)
        negd.remove(r-c+7)
        
backtrack(0)
print(len(res))
        
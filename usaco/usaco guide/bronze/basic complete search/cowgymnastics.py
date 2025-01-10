import sys
sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")

def solve():
    k, n = map(int, input().split())
    arr = []
    for i in range(n):
        temp = []
        for i in range(n):
            temp.append(0)
        arr.append(temp)
    lines = []
    for i in range(k):
        lines.append(list(map(int, input().split())))
        
    res = 0
    row, col = k, n
    for r in range(row):
        for c in range(col):
            for i in range(c+1, col):
                column = lines[r][c]
                eye = lines[r][i]
                arr[eye-1][column-1] += 1
                
    for r in range(col):
        for c in range(col):
            if arr[r][c] >= k:
                res += 1
            
    return res



print(solve())
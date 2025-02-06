import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
def solve():
    n, m = map(int, input().split())
    res = ""

    ticker = 0
    if n > m:
        ticker += 1
    while n and m:
        if ticker % 2:
            res += "B"
            n -= 1
        else:
            res += "G"
            m -= 1
        ticker += 1
        
    if n:
        for i in range(n):
            res += "B"
    else:
        for i in range(m):
            res += "G"
            
    return res


print(solve())
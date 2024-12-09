import sys

sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

def solve():
    n, m = map(int, input().split())
    spotty_cows = [input() for _ in range(n)]
    plain_cows = [input() for _ in range(n, n*2)]
    
    res = 0
    for idx in range(m):
        spotty = []
        for i in range(n):
            spotty.append(spotty_cows[i][idx])
        plain = []
        for i in range(n):
            plain.append(plain_cows[i][idx])
        if all(char not in plain for char in spotty):
            res += 1
    return res

print(solve())

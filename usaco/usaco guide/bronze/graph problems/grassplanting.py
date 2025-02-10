import sys

sys.stdin = open("planting.in", "r")
sys.stdout = open("planting.out", "w")

def solve():
    n = int(input())
    connections = [0] * n
    for i in range(n-1):
        one, two = map(int, input().split())
        connections[one-1] += 1
        connections[two-1] += 1
    
    res = 0
    for i in range(n):
        res = max(res, connections[i])
        
    return res + 1

print(solve())
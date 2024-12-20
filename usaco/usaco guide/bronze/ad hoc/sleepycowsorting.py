import sys

sys.stdin = open("sleepy.in", "r")
sys.stdout = open("sleepy.out", "w")

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    res = 0
    
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            res = i
            break
    return res

print(solve())
import sys

sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")

def solve():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
        
    res = float('inf')
    for i in range(len(arr)):
        temp = 0
        for j in range(len(arr)):
            if j < i:
                temp += (arr[j] * (len(arr) - (i-j)))
            elif i != j:
                temp += (arr[j] * (j-i))
        res = min(res, temp)
    return res

print(solve())
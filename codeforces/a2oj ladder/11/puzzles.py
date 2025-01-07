# n smallest or n largest, whichever difference is smaller

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    res = float("inf")
    l = 0
    for r in range(n-1, len(arr)):
        res = min(res, (arr[r] - arr[l]))
        l += 1
    return res

print(solve())
    
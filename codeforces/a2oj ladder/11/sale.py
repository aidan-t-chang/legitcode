def solve():
    n, m = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    res = 0
    i = 0
    
    while i < n and arr[i] <= 0 and m:
        res += -1 * arr[i]
        m -= 1
        i += 1
        
    return res

print(solve())
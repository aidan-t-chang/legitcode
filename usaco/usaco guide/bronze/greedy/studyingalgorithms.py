import heapq


def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    heapq.heapify(arr)
    res = 0
    sum = 0
    
    while arr:
        t = heapq.heappop(arr)
        if sum + t > x:
            break
        res += 1
        sum += t
    return res
        
print(solve())
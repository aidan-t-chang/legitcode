import heapq
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    
    arr = []
    heapq.heapify(arr)
    
    count = defaultdict(int)

    for _ in range(n):
        p, t = map(int, input().split())
        count[(-p, t)] += 1
        heapq.heappush(arr, (-p, t))
    
    while k:
        process = heapq.heappop(arr)
        k -= 1
        
    return count[process]
    
print(solve())


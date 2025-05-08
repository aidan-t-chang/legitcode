import heapq
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    s = input()
    count = defaultdict(int)
    
    for char in s:
        count[char] += 1
    
    heap = []
    heapq.heapify(heap)
    for c in count:
        heapq.heappush(heap, -count[c])
    res = 0
    while heap:
        c = heapq.heappop(heap)
        c *= -1
        if c >= k:
            res += (k * k)
            break
        k -= c
        res += (c * c)
    
    return res

print(solve())

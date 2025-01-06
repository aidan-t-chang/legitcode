import heapq
def solve():
    k = int(input())
    arr = list(map(int, input().split()))
    if k == 0:
        return 0
    
    # grow same amount or more
    heap = []
    heapq.heapify(heap)
    
    for n in arr:
        heapq.heappush(heap, -n)
    
    res = 0
    while heap:
        n = heapq.heappop(heap)
        if -n >= k:
            res += 1
            return res
        res += 1
        k -= -n
    return -1

print(solve())
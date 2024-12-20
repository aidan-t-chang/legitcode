import heapq
from collections import defaultdict
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    res = []
    count = defaultdict(int)
    
    heapq.heapify(res)
    for i in range(len(arr)):
        count[arr[i]] += 1
    
    # print(count)
    # print(count.values())
    for num in count.values():
        if num > 1:
            return "Still Rozdil"
    
    for i, s in enumerate(arr):
        heapq.heappush(res, (s, i+1))
        
    f = heapq.heappop(res)[1]
    
    return f

print(solve())



        
    
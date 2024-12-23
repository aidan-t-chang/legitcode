import heapq

def solve():
    s, n = map(int, input().split())

    heap = []
    heapq.heapify(heap)
    for i in range(n):
        x, y = map(int, input().split())

        heapq.heappush(heap, (x, y))

    while heap:
        dragon = heapq.heappop(heap)

        if s > dragon[0]:
            s += dragon[1]
        else:
            return "NO"
    
    return "YES"

print(solve())
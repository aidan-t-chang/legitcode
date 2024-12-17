import heapq

n = int(input())

arr = list(map(int, input().split()))

q = []
heapq.heapify(q)
heapq.heappush(q, (abs(arr[0]-arr[-1]), 1, n))

for i in range(n-1):
    heapq.heappush(q, (abs(arr[i+1] - arr[i]), i+1, i+2))

r = heapq.heappop(q)

print(r[1], r[2])
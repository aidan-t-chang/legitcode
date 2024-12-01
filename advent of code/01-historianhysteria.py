import heapq
from collections import defaultdict

# inp = open('inputs.txt', 'r')
# part 1

heap1 = []
heap2 = []
heapq.heapify(heap1)
heapq.heapify(heap2)

for i in range(1000):
    a, b = map(int, input().split())
    heapq.heappush(heap1, int(a))
    heapq.heappush(heap2, int(b))
    
res = 0

while heap1:
    one = heapq.heappop(heap1)
    two = heapq.heappop(heap2)
    
    res += abs(one - two)
    
print('part 1: ', res)

# part 2

one = []
two = defaultdict(int)
for i in range(1000):
    a, b = map(int, input().split())
    one.append(a)
    two[b] += 1
    
res = 0
for n in one:
    res += (n * two[n])
    
print('part 2', res)

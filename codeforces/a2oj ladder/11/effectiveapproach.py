from collections import defaultdict
n = int(input()) # num of elements in array
arr = list(map(int, input().split())) # array | [1, 2]
m = int(input()) # num of queries
queries = list(map(int, input().split()))

res = [0, 0]
hash = defaultdict(int)
for i, n in enumerate(arr):
    hash[n] = i

for q in queries:
    res[0] += (hash[q] + 1)
    res[1] += len(arr) - hash[q]
    

print(res[0], res[1])
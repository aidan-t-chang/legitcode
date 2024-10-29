from collections import Counter
n = int(input())

arr = list(map(int, input().split()))


count = Counter(arr)

for i in range(1, n+1):
    if not count[i]:
        print(i)
        break
    
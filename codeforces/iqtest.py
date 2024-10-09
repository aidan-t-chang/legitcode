from collections import Counter
t = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] = arr[i] % 2
    # [0, 0, 0, 1, 0...] / [1, 1, 1, 0, 1...]
    
count = Counter(arr)

if count[0] > count[1]:
    for i in range(len(arr)):
        if arr[i] == 1:
            print(i + 1)
else:
    for i in range(len(arr)):
        if arr[i] == 0:
            print(i+1)
from collections import Counter
def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    count = Counter(arr[k-1:])
    temp = Counter(arr)
    if len(temp) == 1:
        return 0
    if len(count) == 1:
        for i in range(k-1,-1,-1):
            # print(i, arr[i])
            if arr[i] != arr[k-1]:
                return i+1
    return -1


print(solve())
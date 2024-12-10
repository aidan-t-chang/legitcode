from collections import deque

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = deque()

    for i, n in enumerate(arr):
        arr2.append([i, n])
    
    temp = []
    
    while arr2:
        temp = arr2.popleft()
        if temp[1] - m > 0:
            tt = [temp[0], temp[1] - m]
            arr2.append(tt)
            
    return temp[0]+1

print(solve())

import sys
sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")

def solve():
    n = int(input())
    arr = []
    
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append([a, a+b])
    arr.sort()
    
    # print(arr)
    for i in range(1, len(arr)):
        curr_interval = arr[i]
        curr_start = curr_interval[0]
        curr_end = curr_interval[1]
        if curr_start <= arr[i-1][1]:
            arr[i][0] = arr[i-1][1]
            arr[i][1] = arr[i][0] + (curr_end - curr_start)
            
    # print(arr)
    return arr[-1][1]

print(solve())
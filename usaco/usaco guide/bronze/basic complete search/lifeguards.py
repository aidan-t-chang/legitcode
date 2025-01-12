import sys

sys.stdin = open("lifeguards.in", "r")
sys.stdout = open("lifeguards.out", "w")

def solve():
    n = int(input())
    arr = [0] * 1000
    
    inps = []
    for _ in range(n):
        i, j = map(int, input().split())
        inps.append([i, j])
    
    for pair in inps:
        for l in range(pair[0]+1, pair[1]+1):
            arr[l-1] += 1
               
    # print(arr)
    left_over = float('-inf')
    
    for pair in inps:
        for l in range(pair[0]+1, pair[1]+1):
            arr[l-1] -= 1
        # print(arr)
        count = 1000 - arr.count(0) # number of spots still left over
        # print('c', count)
        left_over = max(left_over, count)
        for l in range(pair[0]+1, pair[1]+1):
            arr[l-1] += 1

            
    return left_over

print(solve())
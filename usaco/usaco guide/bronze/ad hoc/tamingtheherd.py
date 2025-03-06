import sys
sys.stdin = open("taming.in", "r")
sys.stdout = open("taming.out", "w")

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    if arr[0] > 0:
        print(-1)
        return -1
    arr[0] = 0
    
    t = -1
    req = 0
    pos = 0
    
    for i in range(len(arr)-1, -1, -1):
        if t != -1 and arr[i] != -1 and arr[i] != t:
            print(-1)
            return 0
        
        if t == -1:
            t = arr[i]
        if arr[i] == -1:
            arr[i] = t
        if arr[i] == 0:
            req += 1
        if arr[i] == -1:
            pos += 1
        if t > -1:
            t -= 1
    
    print(str(req), str(req+pos))
    return 0

solve()
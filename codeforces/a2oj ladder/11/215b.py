from collections import defaultdict
def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # prefix unique numbers?
    psum = [0]
    checker = set()
    for i in range(len(arr)-1, -1, -1):
        if arr[i] in checker:
            psum.append(psum[-1])
        else:
            psum.append(psum[-1]+1)
            checker.add(arr[i])
    
    for _ in range(m):
        query = int(input())
        print(psum[-query]) 

solve()

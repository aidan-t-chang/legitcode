from collections import defaultdict
def solve():
    arr = defaultdict(int)
    
    q = int(input())
    for _ in range(q):
        qy = list(map(int, input().split()))
        
        if qy[0] == 0:
            arr[qy[1]] = qy[2]
        else:
            print(arr[qy[1]])
    return


solve()

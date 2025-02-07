from collections import defaultdict
import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    if len(arr) % 2:
        print(-1)
        return
    
    john = arr.copy()
    john.sort()
    
    res = defaultdict(list)
    for i in range(0, len(arr)-1, 2):
        if john[i] != john[i+1]:
            print(-1)
            return
        
    for i, n in enumerate(arr):
        res[n].append(i)
    
    # print(res)
    for pair in res.values():
        for i in range(0, len(pair)-1, 2):
            print(pair[i]+1, pair[i+1]+1)
    return
solve()

        
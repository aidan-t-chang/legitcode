import heapq
def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    
    
    res = float("inf")
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # all the new people that need to be put in tandems
            new = [arr[q] for q in range(len(arr)) if q != i and q != j]
            for_this = 0
            for k in range(0, len(arr)-2, 2):
                for_this += new[k+1] - new[k]
            res = min(for_this, res)
    return res


print(solve())
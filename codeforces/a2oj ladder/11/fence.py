def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k == n == 1:
        return 1
    
    psum = [0]
    for nt in arr:
        psum.append(psum[-1]+nt)
    
    res = float("inf")
    # print(psum)
    real_res = 1
    for i in range(len(arr)-k+1):
        sum = psum[i+k] - psum[i]
        # print(sum, i, i+k)
        if sum < res:
            real_res = i+1
            res = min(res, sum)
        
    return real_res

print(solve())
        

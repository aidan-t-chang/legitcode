def solve():
    n = int(input())

    arr = map(int, input().split())

    psum = [0]
    for c in arr:
        psum.append(psum[-1]+c)

    while n > psum[-1]:
        n -= psum[-1]
        
    for i in range(len(psum)):
        if psum[i] >= n:
            return i


print(solve())
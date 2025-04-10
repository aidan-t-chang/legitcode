def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    to_sort = sorted(arr)

    psum1 = [0]
    psum2 = [0]

    for num in arr:
        psum1.append(psum1[-1] + num)
    for num in to_sort:
        psum2.append(psum2[-1] + num)

    for _ in range(m):
        typ, l, r = map(int, input().split())
        if typ == 1:
            print(psum1[r] - psum1[l-1])
        else:
            print(psum2[r] - psum2[l-1])

solve()

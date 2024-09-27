def prefix(arr):
    psum = [0]
    for n in arr:
        psum.append(psum[-1]+n)
    return psum


n, q = map(int, input().split())
seq = list(map(int, input().split()))
piss = prefix(seq)

for i in range(q):
    l, r = map(int, input().split())
    print(piss[r] - piss[l])


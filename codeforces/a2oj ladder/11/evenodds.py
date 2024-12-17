n, k = map(int, input().split())

i = k - 1

if not n % 2:
    if 0 <= i < n//2:
        print((2*i)+1)
    else:
        diff = n-2
        print((2*i)-diff)
else:
    if 0 <= i <= n//2:
        print((2*i)+1)
    else:
        diff = n-1
        print((2*i)-diff)
t = int(input())

res = 0
for i in range(t):

    x = input().split()
    c = x.count('1')
    if c > 1:
        res += 1
print(res)
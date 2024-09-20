n, k = map(int, input().split())
ls = input().split()

res = 0
for score in ls:
    if int(score) >= int(ls[k-1]) and int(score) != 0:
        res += 1

print(res)


s = str(input())

l = 0

res = 0

for r in range(len(s)):
    if s[l] != s[r]:
        res = max(res, r - l)
        l = r
res = max(res, r - l + 1)
print(res)
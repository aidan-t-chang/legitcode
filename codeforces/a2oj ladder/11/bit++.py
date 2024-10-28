t = int(input())

res = 0
for i in range(t):
    l = str(input())
    if '+' in l:  
        res += 1
    else:
        res -= 1
print(res)

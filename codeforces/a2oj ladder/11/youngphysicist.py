t = int(input())

xsum = 0
ysum = 0
zsum = 0

for i in range(t):
    x, y, z = map(int, input().split())
    xsum += x
    ysum += y
    zsum += z
    
    
if xsum != 0 or ysum != 0 or zsum != 0:
    print('NO')
else:
    print('YES')
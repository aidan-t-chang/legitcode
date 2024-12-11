import sys

sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")

arr = sorted(list(map(int, input().split())))

diff1 = arr[1] - arr[0]
diff2 = arr[2] - arr[1]

mi = 0
ma = 0

if diff1 == 1 and diff2 == 1:
    mi = 0
elif diff1 == 2 or diff2 == 2:
    mi = 1
else:
    mi = 2

t = max(diff1, diff2)
ma = t - 1

print(mi)
print(ma)

    

# find distance of 1 from point (2, 2)


co = [0, 0]
for i in range(5):
    arr = list(map(int, input().split()))
    
    if 1 in arr:
        for j in range(len(arr)):
            if arr[j] == 1:
                co = [j, i]
                

res = 0

res += abs(co[0] - 2)
res += abs(co[1] - 2)

print(res)
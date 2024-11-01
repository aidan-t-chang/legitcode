n, m = map(int, input().split())
cows = list(map(int, input().split()))
candy_canes = list(map(int, input().split()))

res = cows
for cane in candy_canes:
    interval = [0, cane]
    temp = []
    for cow in cows:
        if interval[0] < cow and not interval == [0, 0]:
            temp.append(cow + min(cow, interval[1]) - interval[0])
            if interval[1] >= cow:
                interval[0] = cow
            else: # if interval[1] <= cow, there is nothing left to eat
                interval = [0, 0]
                continue
            # print(interval)
        else:
            temp.append(cow)
        #print(temp)
    cows = temp
# print(temp)


for cow in temp:
    print(cow)
    
# O(n * m)
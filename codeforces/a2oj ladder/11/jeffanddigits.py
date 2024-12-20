from collections import Counter

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    count = {0: 0, 5: 0}
    
    for n in arr:
        count[n] += 1
    
    if count[0] < 1:
        return -1
    
    
    while count[5] and count[5] % 9:
        count[5] -= 1
    
    if not count[5]:
        return 0
    
    res = ""
    for five in range(count[5]):
        res += "5"
    for one in range(count[0]):
        res += "0"
    return int(res)

print(solve())

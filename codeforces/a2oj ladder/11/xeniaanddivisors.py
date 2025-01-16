from collections import Counter
def solve():
    n = int(input())
    arr = map(int, input().split())
    
    count = Counter(arr)
    
    res = []
    if count[1] != n//3 or (count[2] + count[3]) != (count[4] + count[6]) or count[5] or count[7] or count[4] > count[2]:
        print(-1)
        return
    
    while len(res) < n//3:
        temp = "1 "
        if count[2] and count[4]:
            temp += "2 4"
            count[2] -= 1
            count[4] -= 1
            res.append(temp)
            continue
        elif count[2]:
            temp += "2 6"
            count[2] -= 1
            count[6] -= 1
            res.append(temp)
            continue
        elif count[3]:
            temp += "3 6"
            count[3] -= 1
            count[4] -= 1
            res.append(temp)
            continue
    
    
    
    for s in res:
        print(s)
    return
        
solve()
s = input()

def scramble(arr):
    def dfs(arr):
        if len(arr) == 0:
            return [[]]
        
        ret = []
        sub = dfs(arr[1:])
        for value in sub:
            for i in range(len(value)+1):
                copy = value.copy()
                copy.insert(i, arr[0])
                ret.append(copy)
        return ret

    res = []
    temp = dfs(arr)
    visit = set()
    
    for value in temp:
        to_check = "".join(value)
        if to_check not in visit:
            res.append(to_check)
            visit.add(to_check)
    return res

arr = scramble([s[i] for i in range(len(s))])
arr.sort()

print(len(arr))
for word in arr:
    print(word)
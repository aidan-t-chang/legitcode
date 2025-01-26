def solve():
    n = input()
    
    res = ""
    for i in range(len(n)):
        if n[i] == "0":
            res += n[i+1:]
            return res
        res += n[i]
        
    return res[:-1]

print(solve())
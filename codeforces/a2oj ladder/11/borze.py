s = input()

res = ""
i = 0
if s[i] == ".":
    res += "0"
    i += 1
    
while i <= len(s) - 1:
    if s[i] == "-" and s[i+1] == ".":
        res += "1"
        i += 2
    elif s[i] == "-" and s[i+1] == "-":
        res += "2"
        i += 2
    else:
        res += "0"
        i += 1
    
print(res)

def solve():
    s = input()
    
    for c in s:
        if c != "1" and c != "4":
            return "NO"
        
    if s[0] == "4" or (s[0] == "4" and s[1] == "4"):
        return "NO"
        
    l = 0
    for r in range(len(s)):
        if s[r] != "4":
            l = r
        if r - l == 3:
            return "NO"
            
    return "YES"

print(solve())
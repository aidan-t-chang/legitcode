from collections import Counter
def solve():
    s1 = input()
    s2 = input()
    
    count1 = Counter(s1)
    
    for char in s2:
        if char == " ":
            continue
        if not count1[char]:
            return "NO"
        count1[char] -= 1
        
    return "YES"


print(solve())
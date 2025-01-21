from collections import defaultdict

def solve():
    s1 = input()
    s2 = input()
    
    if len(s1) != len(s2):
        return "NO"
    count1, count2 = defaultdict(int), defaultdict(int)
    
    for char in s1:
        count1[char] += 1
    for char in s2:
        count2[char] += 1
    
    if not count1 == count2:
        return "NO"
    
    count = 0
    for i in range(len(s1)):
        if count > 2:
            return "NO"
        if s1[i] != s2[i]:
            count += 1
            
    return "YES"

print(solve())
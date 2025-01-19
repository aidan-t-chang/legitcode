from collections import defaultdict
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    a = 0
    b = 0
    for n in arr:
        if n == 100:
            a += 1
        else:
            b += 1
            
    sum = 100*a + 200*b
    if sum % 200:
        return "NO"
    
    for i in range(b+1):
        if 200 * i <= sum // 2 and sum // 2 - 200 * i <= a * 100:
            return "YES"
        
    return "NO"

print(solve())
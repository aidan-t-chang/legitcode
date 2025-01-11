from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    count = Counter(arr)
    
    diff = max(arr) - min(arr)
    
    if diff == 0:
        two = n * (n-1) / 2
    else:
        two = count[max(arr)] * count[min(arr)]
        
    return " ".join([str(diff), str(int(two))])
    


print(solve())
    
    
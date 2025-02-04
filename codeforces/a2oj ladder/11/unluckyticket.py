def solve():
    n = int(input())
    arr = input()

    l1 = []
    l2 = []
    
    for i in range(n):
        l1.append(arr[i])
    for i in range(n, 2*n):
        l2.append(arr[i])    

    l1.sort()
    l2.sort()
    
    if l1[0] > l2[0]: # everything should be increasing from l1 to l2
        if all(l1[i] > l2[i] for i in range(n)):
            return "YES"
    elif l2[0] > l1[0]: # everything should be decreasing from l1 to l2
        if all(l2[i] > l1[i] for i in range(n)):
            return "YES"
    return "NO"

print(solve())
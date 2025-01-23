def solve():
    n = int(input())
    x = []
    y = []
    points = []
    for _ in range(n):
        lnx, lny = map(int, input().split())
        x.append(lnx)
        y.append(lny)
        points.append((lnx, lny))
    x.sort()
    y.sort(reverse=True)
    
    for i in range(len(points)):
        if points[i] == (x[0], y[0]):
            return i+1
        
    return -1

print(solve())
        
    
        
    
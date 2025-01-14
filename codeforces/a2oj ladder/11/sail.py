def solve():
    t, sx, sy, ex, ey = map(int, input().split())
    wind = [char for char in input()]
    dir = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    
    
    horizontal = (sx - ex)
    vertical = (sy - ey)
    
    if horizontal > 0:
        dir['W'] += horizontal
    else:
        dir['E'] += -horizontal
    if vertical > 0:
        dir['S'] += vertical
    else:
        dir['N'] += -vertical
         
    # print(dir)
    for i in range(len(wind)):
        if dir[wind[i]]:
            dir[wind[i]] -= 1
            
        if all(not val for val in dir.values()):
            return i+1
    return -1
            

print(solve())
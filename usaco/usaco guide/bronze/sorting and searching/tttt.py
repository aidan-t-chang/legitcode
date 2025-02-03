from collections import defaultdict
import sys

sys.stdin = open("tttt.in", "r")
sys.stdout = open("tttt.out", "w")

def solve():
    grid = []
    for _ in range(3):
        line = input()
        grid.append(line)

    row = col = 3
    
    single = set()
    two = set()
    
    # straight across
    for r in range(row):
        indiv_count = defaultdict(int)
        for c in range(col):
            indiv_count[grid[r][c]] += 1
        
        if len(indiv_count) == 1:
            for one in indiv_count.keys():
                if one not in single:
                    single.add(one)
        elif len(indiv_count) == 2:
            one = two2 = ""
            for two22 in indiv_count.keys():
                if one == "":
                    one = two22
                else:
                    two2 = two22
            if (one, two2) not in two and (two2, one) not in two:
                two.add((one, two2))    
    # print(two)        
    
    #straight down
    for c in range(col):
        down = defaultdict(int)
        for r in range(row):
            down[grid[r][c]] += 1
        
        if len(down) == 1:
            for one in down.keys():
                if one not in single:
                    single.add(one)
        elif len(down) == 2:
            one = two2 = ""
            for two22 in down.keys():
                if one == "":
                    one = two22
                else:
                    two2 = two22
            if (one, two2) not in two and (two2, one) not in two:
                two.add((one, two2))    
    
    # print(two)
    # diagonal
    diag = defaultdict(int)
    for i in range(3):
        diag[grid[i][i]] += 1
    
    if len(diag) == 1:
        for one in diag.keys():
            if one not in single:
                single.add(one)
    elif len(diag) == 2:
        one = two2 = ""
        for two22 in diag.keys():
            if one == "":
                one = two22
            else:
                two2 = two22
        if (one, two2) not in two and (two2, one) not in two:
            two.add((one, two2))   

    # print(two)    
    neg = defaultdict(int)
    for i in range(3):
        neg[grid[2-i][i]] += 1
        
    if len(neg) == 1:
        for one in neg.keys():
            if one not in single:
                single.add(one)
    elif len(neg) == 2:
        one = two2 = ""
        for two22 in neg.keys():
            if one == "":
                one = two22
            else:
                two2 = two22
        if (one, two2) not in two and (two2, one) not in two:
            two.add((one, two2))   
        
            
    print(len(single))
    print(len(two))
    
solve()


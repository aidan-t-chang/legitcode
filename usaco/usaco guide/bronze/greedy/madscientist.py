import sys

sys.stdin = open("breedflip.in", "r")
sys.stdout = open("breedflip.out", "w")

def solve():
    n = int(input())
    a = input()
    b = input()
    
    i = 0
    while a[i] == b[i]:
        i += 1
        
    res = 0
    while i < len(a):
        if a[i] == b[i] and a[i-1] != b[i-1]:
            res += 1
        i += 1
    
    return res


print(solve())
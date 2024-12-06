import sys

sys.stdin = open("censor.in", "r")
sys.stdout = open("censor.out", "w")

# whatthemomooofun
# moo

def solve():
    s = input()
    t = input()
    
    censored = ""
    
    for c in s:
        censored += c
        if censored[-len(t):] == t:
            censored = censored[:-len(t)]
                                
    return censored    
    
    
    
print(solve())
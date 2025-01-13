import sys

sys.stdin = open('guess.in', "r")
sys.stdout = open('guess.out', 'w')

def solve():
    # how many elements are shared between animals // how many charstics are not 0, return that + 1
    n = int(input())
    animals = []
    for _ in range(n):
        arr = list(map(str, input().split()))[2:]
        arr = set(arr)
        animals.append(arr)
    
    max_yes = 0
    
    for i in range(len(animals)):
        for j in range(i+1, len(animals)):
            max_yes = max(max_yes, len(animals[i].intersection(animals[j]))+1)
            
    return max_yes


print(solve())


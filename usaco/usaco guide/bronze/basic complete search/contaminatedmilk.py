import sys

sys.stdin = open("badmilk.in", "r")
sys.stdout = open("badmilk.out", "w")


def solve():
    n, m, d, s = map(int, input().split())
    # this person drank this milk at this time 
    array = [[] for _ in range(n)]
    freq2 = {j:0 for j in range(1, m+1)}
    for _ in range(d):
        time2 = list(map(int, input().split()))
        idx = time2[0]-1
        freq2[time2[1]] += 1
        if time2 not in array[idx]:
            array[idx].append(time2)
    sick = []
    for _ in range(s):
        time3 = list(map(int, input().split()))
        sick.append(time3)
    
    freq = {j:0 for j in range(1, m+1)}
    for person, time in sick:
        for p2, m, t in array[person-1]:
            if t < time:
                freq[m] += 1
    
    compare = 0
    val = 0
    for n in freq:
        if freq[n] > compare:
            compare = freq[n]
            val = n
    
    return freq2[val]
    
    

    

print(solve())
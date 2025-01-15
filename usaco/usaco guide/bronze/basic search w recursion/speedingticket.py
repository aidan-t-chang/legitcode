import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

def solve():
    n, m = map(int, input().split())
    speed = [0] * 100
    bound = 1
    for _ in range(n):
        s, limit = map(int, input().split())
        # print(bound+s)
        for i in range(bound, bound+s):
            # print(i)
            speed[i-1] = limit
        bound += s

    bess = [0] * 100
    bound = 1
    for _ in range(m):
        s, limit = map(int, input().split())
        for i in range(bound, bound+s):
            bess[i-1] = limit
        bound += s

    # print(speed, bess)
    res = 0
    for i in range(len(speed)):
        if bess[i] > speed[i]:
            res = max(res, bess[i] - speed[i])
            
    return res


print(solve())
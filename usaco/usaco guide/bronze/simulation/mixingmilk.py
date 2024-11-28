import sys

sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")


for i in range(3):
    if i == 0:
        one = list(map(int, input().split()))
    elif i == 1:
        two = list(map(int, input().split()))
    else:
        three = list(map(int, input().split()))
        
cur = 0
for i in range(100):
    if cur == 0:
        temp = min(one[1], two[0] - two[1])
        two[1] += temp
        one[1] -= temp
        # print(cur, 'iteration', one[1], two[1])
    elif cur == 1:
        temp = min(two[1], three[0] - three[1])
        three[1] += temp
        two[1] -= temp
        # print(cur, 'iteration', two[1], three[1])
    else:
        temp = min(three[1], one[0] - one[1]) 
        one[1] += temp
        three[1] -= temp
        # print(cur, 'iteration', three[1], one[1])
    cur = (cur + 1) % 3
        
print(one[1])
print(two[1])
print(three[1])
import sys

sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")

dd = []

m, n, k = map(int, input().split())

for i in range(m):
    dd.append([input()])

rows = len(dd)
# print(dd)
for r in range(rows):
    temp = []
    for char in dd[r]:
        for c in char:
            if c == "X":
                temp += ["X"] * k
            else:
                temp += ["."] * k
        for i in range(k):
            t = "".join(temp)
            print(t)
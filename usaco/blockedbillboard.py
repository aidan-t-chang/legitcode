import sys

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")



x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

bill1 = (x2-x1) * (y2-y1)
bill2 = (x4-x3) * (y4-y3)

bill1_area = bill1 - max(0, min(x6, x2) - max(x5, x1)) * max(0, min(y6, y2) - max(y5, y1))


bill2_area = bill2 - max(0, min(x6, x4) - max(x5, x3)) * max(0, min(y6, y4) - max(y5, y3))

print(bill1_area + bill2_area)


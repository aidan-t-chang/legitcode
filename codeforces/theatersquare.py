import math

n,m,a = map(int, input().split())

one = math.ceil(n/a)
two = math.ceil(m/a)
print(one*two)

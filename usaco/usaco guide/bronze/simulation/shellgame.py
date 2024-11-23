import sys

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

t = int(input())

for i in range(t):
    a, b, g = map(int, input().split())
    
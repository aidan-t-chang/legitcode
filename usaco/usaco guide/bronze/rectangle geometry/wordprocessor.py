import sys

sys.stdin = open("word.in", "r")
sys.stdout = open("word.out", "w")

n, k = map(int, input().split())
string = str(input()) # hello my name is Bessie and this is my essay


def len_no_space(s):
    res = 0
    for i in range(len(s)):
        if s[i] != " ":
            res += 1
    return res

spl = string.split() #[hello, my, name, is, Bessie, and, this, is, my, essay]

i = 0
while i < len(spl):
    temp = ""
    while i < len(spl) and len_no_space(temp) + len(spl[i]) <= k:
        temp = temp + spl[i] + " "
        i += 1
    print(temp.strip())
    


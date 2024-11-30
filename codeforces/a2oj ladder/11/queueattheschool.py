n, t = map(int, input().split())

s = input()


res = s
for i in range(t):
    l, r = len(s) - 2, len(s) - 1
    stack = []

    while r >= 0:
        if l >= 0 and s[l] == "B" and s[r] == "G":
            stack.append("B")
            stack.append("G")
            r -= 1
            l -= 1

        else:
            stack.append(s[r])
        r -= 1
        l -= 1
    res = "".join(stack)
    res = res[::-1]
    s = res

print(res)
_ = str(input())
s = [c.lower() for c in _]

res = []

for char in s:
    if char != "a" and char != "e" and char != "i" and char != "o" and char != "u" and char != "y":
        res.append('.' + char)

print("".join(res))

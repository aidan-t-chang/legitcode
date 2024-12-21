def solve():
    s = input()
    t = input()

    return "YES" if s == t[::-1] else "NO"

print(solve())
def solve():
    n = int(input())
    sortbyp = []
    sortbyq = []

    for _ in range(n):
        a, b = map(int, input().split())
        sortbyp.append((a, b))
        sortbyq.append((b, a))

    sortbyp.sort()
    sortbyq.sort()
    for i in range(len(sortbyp)):
        a, b = sortbyp[i]
        a2, b2 = sortbyq[i]
        if a != b2 or a2 != b:
            return "Happy Alex"
    return "Poor Alex"

print(solve())

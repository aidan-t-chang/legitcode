def solve():
    n = int(input())
    numbers = sorted(map(int, input().split()))
    res = 1
    for i in range(1, n):
        if numbers[i] != numbers[i - 1]:
            res += 1
    return res

print(solve())


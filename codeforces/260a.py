import sys
sys.set_int_max_str_digits(999999)
def solve():
    a, b, n = map(int, input().split())

    a *= 10
    for i in range(10):
        a += i
        if not a % b:
            for _ in range(n-1):
                a *= 10
            return a
        a -= i
    return -1

print(solve())

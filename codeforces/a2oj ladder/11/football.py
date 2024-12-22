def solve():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())

    arr.sort()

    mid = len(arr) // 2
    return arr[mid]

print(solve())
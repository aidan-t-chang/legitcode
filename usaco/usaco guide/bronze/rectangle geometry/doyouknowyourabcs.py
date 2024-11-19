arr = list(map(int, input().split())) # 2, 2, 11, 4, 9, 7, 9

arr.sort()

a, b = arr[0], arr[1]

if a + b == arr[2]:
    print(a, b, arr[3])
else:
    print(a, b, arr[2])
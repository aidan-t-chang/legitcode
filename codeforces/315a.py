from collections import defaultdict

def main(): # hash a counts and then put visited numbers into a set
    n = int(input())
    arr = []
    visit = set()
    count = defaultdict(int)

    for _ in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])
        count[a] += 1
    
    decrement = n

    for i in range(n):
        a, b = arr[i]
        for j in range(n):
            a2, b2 = arr[j]
            if i != j and b2 == a:
                decrement -= 1
                break
    return decrement

print(main())

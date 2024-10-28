n = int(input())


res = [n]

print(n, end=" ")
while n != 1:
    if n % 2:
        n *= 3
        n += 1
    else:
        n /= 2
    
    print(int(n), end=" ")
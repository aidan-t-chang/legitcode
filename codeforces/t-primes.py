import math

t = int(input())
arr = list(map(int, input().split()))

def sieve(n): 
    prime = [True for i in range(n+1)] 
    prime[0], prime[1] = False, False
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime

primes = sieve(10**6)
for num in arr:
    sqrt = math.sqrt(num)
    if sqrt == int(sqrt):
        if primes[int(sqrt)]:
            print("YES")
            continue
    print("NO")
        

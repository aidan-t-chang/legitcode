# The prime factors of 13195 are 5, 7, and 29.
# What is the largest prime factor of the number 600851475143?
import time
from reader import feed

n = 600851475143
i = 2
def func(n, i):
    start = time.perf_counter()
    while i ** 2 < n:
        while n % i == 0:
            n = n / i
        i += 1
    end = time.perf_counter()
    return n, end - start


print(func(n, i))



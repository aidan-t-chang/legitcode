import time
from reader import feed

# Find the largest palindromic number from the product of two 3-digit numbers.

n1 = 999
n2 = 99
palindromes = []
start = time.perf_counter()
while n1 > n2:
    for i in range(n1, n2, -1):
        product = n1 * i
        if str(product) == str(product)[::-1]:
            palindromes.append(product)
            n2 = i
            break
    n1 -= 1
end = time.perf_counter()
print(palindromes, end - start)
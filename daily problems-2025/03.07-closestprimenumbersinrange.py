# Given two positive integers left and right, find the two integers num1 and num2 such that:

# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. 
# If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

class Solution:
    def closestPrimes(self, left: int, right: int):
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, right+1, i):
                    sieve[j] = False
        
        primes = [i for i in range(left, right + 1) if sieve[i]]

        result = [-1, -1]
        if len(primes) < 2:
            return result

        diff = float('inf')
        for i in range(1, len(primes)):
            gap = primes[i] - primes[i-1]
            if gap < diff:
                diff = gap
                result = [primes[i-1], primes[i]]

        return result




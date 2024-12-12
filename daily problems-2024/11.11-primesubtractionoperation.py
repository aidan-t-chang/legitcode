# You are given a 0-indexed integer array nums of length n.

# You can perform the following operation as many times as you want:

# Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], 
# then subtract p from nums[i].
# Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

# A strictly increasing array is an array whose each element is strictly greater than its preceding element.

import bisect

class Solution:
    def primeSubOperation(self, nums) -> bool:
        
        def sieve(max_num):
            is_prime = [True] * (max_num + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(max_num**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, max_num + 1, i):
                        is_prime[j] = False
            return [i for i in range(2, max_num + 1) if is_prime[i]]
        
        primes = sieve(1000)
        
        prev = 0 
        for i in range(len(nums)):
            pos = bisect.bisect_left(primes, nums[i])
            success = False
            
            for j in range(pos - 1, -1, -1):
                prime = primes[j]
                if nums[i] - prime > prev:
                    nums[i] -= prime
                    success = True
                    break
            
            if not success and nums[i] <= prev:
                return False
            
            prev = nums[i]
        
        return True
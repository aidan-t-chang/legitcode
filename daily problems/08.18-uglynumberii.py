# An ugly number is a positive integer whose prime factors are 
# limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minheap = [1] # "base case" number
        visit = set()
        factors = [2, 3, 5]
        for i in range(n):
            num = heapq.heappop(minheap)
            if i == n - 1: # nth ugly number has been found
                return num

            for f in factors:
                if (num * f) not in visit:
                    visit.add(num * f)
                    heapq.heappush(minheap, num * f)
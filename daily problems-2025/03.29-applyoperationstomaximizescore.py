# You are given an array nums of n positive integers and an integer k.

# Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:

# Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
# Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
# Multiply your score by x.
# Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.

# The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

# Return the maximum possible score after applying at most k operations.

# Since the answer may be large, return it modulo 109 + 7.
from math import sqrt
import heapq

class Solution:
    def maximumScore(self, nums, k: int) -> int:
        N = len(nums)
        MOD = 10**9 + 7
        res = 1

        prime_scores =[]
        for n in nums:
            score = 0
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    score += 1
                    while n % f == 0:
                        n //= f
            if n >= 2:
                score += 1
            prime_scores.append(score)

        
        left_bound = [-1] * N
        right_bound = [N] * N

        stack = []
        for i, s in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < s: # the right boundary has been found
                index = stack.pop()
                right_bound[index] = i
            if stack: 
                left_bound[i] = stack[-1]
            stack.append(i)


        min_heap = [(-n, i) for i, n in enumerate(nums)]
        heapq.heapify(min_heap)

        while k > 0:
            n, index = heapq.heappop(min_heap)
            n = -n
            score = prime_scores[index]
            
            left_count = index - left_bound[index]
            right_count = right_bound[index] - index

            count = left_count * right_count
            operations = min(count, k)
            res = (res * pow(n, operations, MOD)) % MOD

            k -= operations


        return res
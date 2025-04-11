# You are given two positive integers low and high.

# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

# Return the number of symmetric integers in the range [low, high].
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i, num in enumerate(range(low, high+1)):
            check = str(num)
            if len(check) % 2:
                continue
            n = len(check)//2
            first = [int(check[j]) for j in range(n)]
            last = [int(check[i]) for i in range(n, len(check))]
            # print(first, last)
            if sum(first) == sum(last):
                res += 1
        return res
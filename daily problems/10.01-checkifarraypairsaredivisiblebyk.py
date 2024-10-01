# Given an array of integers arr of even length n and an integer k.

# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

# Return true If you can find a way to do that or false otherwise.

class Solution:
    def canArrange(self, arr, k):
        rcount = {}

        for i in arr:
            complement = (i % k + k) % k
            rcount[complement] = (rcount.get(complement, 0) + 1)



        for i in arr:
            rem = (i % k + k) % k
            if rem == 0:
                if rcount[0] % 2:
                    return False

            elif rcount[rem] != rcount.get(k-rem, 0): # if the amount of remainder values equals the amount of complement remainder values (pairs)
                return False
            
        return True
            
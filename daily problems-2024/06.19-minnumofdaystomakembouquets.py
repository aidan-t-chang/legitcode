# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. 
# To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, 
# the ith flower will bloom in the bloomDay[i] and 
# then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to
# make m bouquets from the garden. If it is impossible to make m bouquets return -1.

class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1 # consecutive bouquets cannot even be made
        
        def possible(bloomDay, m, k, day):
            total = 0
            flowers = 0
            for d in bloomDay:
                if d <= day:
                    flowers += 1
                    if flowers == k:
                        total += 1
                        flowers = 0
                else:
                    flowers = 0
            return total >= m
        
        l, r = 1, max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if possible(bloomDay, m, k, mid):
                r = mid
            else:
                l = mid + 1
        return l
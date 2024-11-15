# You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, 
# where quantities[i] represents the number of products of the ith product type.

# You need to distribute all products to the retail stores following these rules:

# A store can only be given at most one product type but can be given any amount of it.
# After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. 
# You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
# Return the minimum possible x.
import math

class Solution:
    def minimizedMaximum(self, n: int, quantities) -> int:
        def can_distribute(x):
            stores = 0
            for quantity in quantities:
                stores += math.ceil(quantity/x)
            return stores <= n # if the amount of stores needed is less than the amount of stores we have now

        l, r = 1, max(quantities)

        res = 0
        while l <= r:
            m = (l + r) // 2
            if can_distribute(m): # the m value is viable
                res = m
                r = m - 1
            else:
                l = m + 1 

        return res
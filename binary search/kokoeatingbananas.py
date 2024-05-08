# Koko loves to eat bananas. 
# There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. 
# Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

import math
def koko(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        m = (l + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / m)
        if hours <= h:
            res = min(res, m)
            r = m - 1 # find a possibly smaller rate
        else:
            l = m + 1 # find the bigger rate
    return res


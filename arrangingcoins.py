# You have n coins and you want to build a staircase with these coins. 
# The staircase consists of k rows where the ith row has exactly i coins. 
# The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

def arrangeCoins(n):
    L = 1
    R = n
    while L <= R:
        mid = (L + R) // 2
        na = (mid * (mid + 1)) / 2
        if na == n:
            return mid
        elif na < n:
            L = mid + 1
        else:
            R = mid - 1
    return R
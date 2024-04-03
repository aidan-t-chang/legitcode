# Given a non-negative integer x, 
# # return the square root of x rounded down to the nearest integer. 
# # The returned integer should be non-negative as well.

def sqrt(x):
    left = 0
    right = x
    while left < right:
        mid = (left + right + 1) // 2
        if mid <= x // mid:
            left = mid
        else:
            right = mid - 1
    return left
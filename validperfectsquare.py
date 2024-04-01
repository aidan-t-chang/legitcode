# Given a positive integer num, return true if num is a perfect square or false otherwise.

def square(num):
    if num == 0:
        return True
    L = 1
    R = num
    while True:
        if R < L:
            return False
        mid = (L + R) // 2
        if mid == num / mid:
            return True
        if mid < num / mid:
            L = mid + 1
        else:
            R = mid - 1 

print(square(9))
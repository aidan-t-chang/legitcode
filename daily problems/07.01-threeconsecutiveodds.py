# Given an integer array arr, 
# return true if there are three consecutive odd numbers in the array. 
# Otherwise, return false.

class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        if len(arr) <= 2:
            return False
        l, r = 0, 2
        
        while r < len(arr):
            if arr[l] % 2 == 1 and arr[l+1] % 2 == 1 and arr[r] % 2 == 1:
                return True
            else:
                l += 1
                r += 1
        return False
        
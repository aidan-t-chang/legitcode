# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        for l in range(len(arr)-2):
            if all(j % 2 for j in arr[l:l+3]):
                return True
        return False
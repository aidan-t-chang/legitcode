# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

from collections import defaultdict

class Solution:
    def checkIfExist(self, arr) -> bool:
        count = defaultdict(int)

        for n in arr:
            count[n] += 1

        for i in range(len(arr)):
            if count[(arr[i]*2)] and i != arr.index(arr[i]*2):
                return True
        return False
    
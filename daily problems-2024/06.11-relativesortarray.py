# Given two arrays arr1 and arr2, the elements of arr2 are distinct, 
# and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of 
# items in arr1 are the same as in arr2. 
# Elements that do not appear in arr2 should be placed at 
# the end of arr1 in ascending order.

from collections import Counter

class Solution:
    def relativeSortArray(self, arr1, arr2):
        counted = Counter(arr1)
        res = []
        external = []
        for element in arr2:
            for i in range(counted[element]):
                res.append(element)
        
        for element in arr1:
            if element not in res:
                external.append(element)
        
        res = res + sorted(external)
        return res
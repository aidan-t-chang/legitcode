# A distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. 
# If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.




from collections import Counter
class Solution:
    def kthDistinct(self, arr, k: int) -> str:
        count = Counter(arr)

        for a in arr:
            if count[a] == 1:
                k -= 1
                if k == 0:
                    return a
        return ''
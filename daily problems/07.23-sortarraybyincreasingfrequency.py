# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
# If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

from collections import Counter



class Solution:
    def frequencySort(self, nums):
        count = Counter(nums)

        def custom_sort(n):
            return (count[n], -n)

        nums.sort(key=custom_sort)

        return nums
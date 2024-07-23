# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
# If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

from collections import Counter



def frequencySort(nums):
    count = Counter(nums)
    count.sort()
    return count

print(frequencySort([1,1,2,2,2,3]))
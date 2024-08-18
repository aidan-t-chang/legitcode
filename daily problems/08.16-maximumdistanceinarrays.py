# You are given m arrays, where each array is sorted in ascending order.

# You can pick up two integers from two different arrays 
# (each array picks one) and calculate the distance. 
# We define the distance between two integers a and b to be 
# their absolute difference |a - b|.

# Return the maximum distance.

class Solution(object):
    def maxDistance(self, arrays):
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return max_distance       
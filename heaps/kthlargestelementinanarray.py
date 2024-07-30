# Given an integer array nums and an integer k, 
# return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.

# Can you solve it without sorting?

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        new = [n * -1 for n in nums]
        heapq.heapify(new) # max heap from negative numbers
        for i in range(k-1):
            heapq.heappop(new)
        return new[0] * -1
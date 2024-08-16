# The distance of a pair of integers a and b is defined as the 
# absolute difference between a and b.

# Given an integer array nums and an integer k, 
# return the kth smallest distance among all the pairs nums[i] and nums[j] 
# where 0 <= i < j < nums.length.


class Solution:
    def smallestDistancePair(self, numbers, k: int) -> int:
        numbers.sort()
        minDistance, maxDistance = 0, numbers[-1] - numbers[0]
        
        while minDistance < maxDistance:
            midDistance = (minDistance + maxDistance) // 2
            if self.countPairsWithinDistance(numbers, midDistance) < k:
                minDistance = midDistance + 1
            else:
                maxDistance = midDistance
        
        return minDistance

    def countPairsWithinDistance(self, numbers, targetDistance: int) -> int:
        count = left = 0
        for right in range(1, len(numbers)):
            while numbers[right] - numbers[left] > targetDistance:
                left += 1
            count += right - left
        return count
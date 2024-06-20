# In the universe Earth C-137, 
# Rick discovered a special form of magnetic force between 
# two balls if they are put in his new invented basket. 
# Rick has n empty baskets, the ith basket is at position[i],
# Morty has m balls and needs to distribute the balls into the 
# such that the minimum magnetic force between any two balls is maximum.

# Rick stated that magnetic force between two different balls 
# at positions x and y is |x - y|.

# Given the integer array position and the integer m. 
# Return the required force.

class Solution:
    def abletoplace(self, arr, dist, balls):
        count = 1
        L = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - L >= dist:
                count += 1
                L = arr[i]
        return count >= balls
    def maxDistance(self, position, m):
        position.sort()
        l, r = 1, (position[-1] - position[0]) // (m - 1) 
        # maximum possible distance if all balls are equidistant
        ans = 1

        while l <= r:
            mid = l + (r - l) // 2 
            # mid of entire array, 
            # adjusted by how far the left is by the original left bound
            if self.abletoplace(position, mid, m):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
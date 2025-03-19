# You are given a binary array nums.

# You can do the following operation on the array any number of times (possibly zero):

# Choose any 3 consecutive elements from the array and flip all of them.
# Flipping an element means changing its value from 0 to 1, and from 1 to 0.

# Return the minimum number of operations required to make all elements in nums equal to 1. 
# If it is impossible, return -1.
from collections import deque

class Solution:
    def minOperations(self, nums) -> int:
        q = deque()
        count = 0

        for i in range(len(nums)):
            while q and i > q[0] + 2:
                q.popleft()
            
            if (nums[i] + len(q)) % 2 == 0:
                if i + 2 >= len(nums):
                    return -1 # triplet cannot be made
                count += 1
                q.append(i)
        
        return count
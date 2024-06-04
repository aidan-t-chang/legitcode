# Given an array of integers nums containing n + 1 integers 
# where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only 
# constant extra space.

class Solution:
    def findDuplicate(self, nums) -> int:
        slow, fast = 0, 0

        #phase 1
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #fast and slow intersect at this point

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
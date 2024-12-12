# Sort a list nums with values 0, 1, and 2 in place.


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = {0: 0, 1: 0, 2: 0}

        for value in nums:
            buckets[value] += 1
        
        for bucket in buckets:
            for i in range(buckets[bucket]):
                nums.remove(nums[0])
                nums.append(bucket)
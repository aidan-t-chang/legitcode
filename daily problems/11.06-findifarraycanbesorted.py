# You are given a 0-indexed array of positive integers nums.

# In one operation, you can swap any two adjacent elements if they have the same number of 
# set bits
# . You are allowed to do this operation any number of times (including zero).

# Return true if you can sort the array, else return false.

class Solution:
    def canSortArray(self, nums) -> bool:
        prev = currmin = currmax = 0
        prevbit = -1

        for n in nums:
            count = n.bit_count()
            if prevbit != count:
                if currmin < prev:
                    return False
                prev = currmax
                currmin = currmax = n
                prevbit = count
            else:
                currmin = min(currmin, n)
                currmax = max(currmax, n)
        
        return currmin >= prev
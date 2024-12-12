# You are given a 0-indexed integer array mapping which represents the 
# mapping rule of a shuffled decimal system. 
# mapping[i] = j means digit i should be mapped to digit j in this system.

# The mapped value of an integer is the new integer obtained by 
# replacing each occurrence of digit i in the integer with 
# mapping[i] for all 0 <= i <= 9.

# You are also given another integer array nums. 
# Return the array nums sorted in non-decreasing order based on the mapped values of its elements.


class Solution:
    def sortJumbled(self, mapping, nums):
        pairs = []

        for i, n in enumerate(nums): # easily obtain the indexes of each num
            n = str(n)

            mapped_n = 0
            for char in n:
                mapped_n *= 10 # multiplying by 10 frees up a spot to add the next number
                mapped_n += mapping[int(char)] # 6 -> 60- -> 66
            
            pairs.append((mapped_n, i))
        
        pairs.sort()
        return [nums[p[1]] for p in pairs] # p[1]: second value in the pair, the index mapped to a num in nums
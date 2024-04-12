# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

def longest(nums):
    s = set(nums)
    longest = 0

    for num in nums:
        # check if num is the start of a sequence
        if num - 1 not in s: # if there is no prior number before num, it is the start of the sequence
            length = 0 # length of the sequence
            while num + length in s: # num + length is the current number 
                length += 1 # if the current number is in s, the length of the sequence increases by 1
            longest = max(length, longest) 
            # if longest is larger than the length we just iterated on, keep longest. if length is longer, the longest becomes length
    return longest
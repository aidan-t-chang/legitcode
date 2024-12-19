# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. 
# After concatenating them, the result should equal the sorted array.

# Return the largest number of chunks we can make to sort the array.

class Solution:
    def maxChunksToSorted(self, arr) -> int:
        chunks = 0
        psum = 0
        s_sum = 0
        
        for i in range(len(arr)):
            psum += arr[i]
            s_sum += i

            if psum == s_sum:
                chunks += 1

        return chunks
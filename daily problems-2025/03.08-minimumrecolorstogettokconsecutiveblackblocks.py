# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. 
# The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curw = 0
        for char in range(k):
            if blocks[char] == 'W':
                curw += 1
        res = curw
        l = 1
        for r in range(k, len(blocks)):
            if blocks[l-1] == "W":
                curw -= 1
            if blocks[r] == "W":
                curw += 1
            res = min(res, curw)
            l += 1

        return res
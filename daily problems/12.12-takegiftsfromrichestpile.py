# You are given an integer array gifts denoting the number of gifts in various piles. 
# Every second, you do the following:

# Choose the pile with the maximum number of gifts.
# If there is more than one pile with the maximum number of gifts, choose any.
# Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
# Return the number of gifts remaining after k seconds.
import heapq, math

class Solution:
    def pickGifts(self, gifts, k: int) -> int:
        arr = []
        heapq.heapify(arr)
        for n in gifts:
            heapq.heappush(arr, -1 * n)

        for _ in range(k):
            t = -1 * heapq.heappop(arr)
            new = math.floor(math.sqrt(t))
            heapq.heappush(arr, -1 * new)

        res = 0
        while arr:
            res += -1 * heapq.heappop(arr)
        return res
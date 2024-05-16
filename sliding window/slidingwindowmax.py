# You are given an array of integers nums, 
# there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

import collections
def maxsliding(nums, k):
    res = []
    q = collections.deque() # contains indicess
    l = r = 0

    while r < len(nums):
        # remove smaller values from the deque
        while q and nums[q[-1]] < nums[r]: # while smaller values exist in the queue:
            q.pop()
        q.append(r)
        
        if l > q[0]: # if leftmost value is out of bounds from the queue, we remove the value since it can't be considered
            q.popleft()


        if r + 1 >= k: # to update output, window size must at least be size k
            res.append(nums[q[0]])
            l += 1
        r += 1

    return res



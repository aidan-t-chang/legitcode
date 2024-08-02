# You are given an array of CPU tasks, each represented by letters A to Z, 
# and a cooling time, n. Each cycle or interval allows the completion of one task. 
# Tasks can be completed in any order, but there's a constraint: 
# identical tasks must be separated by at least n intervals due to cooling time.

# ​Return the minimum number of intervals required to complete all tasks.

import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idletime]

        while maxHeap or q: # as long as one isnt empty there are tasks to be done
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # decrease frequency by 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0]) # add the count back to the heap
        return time

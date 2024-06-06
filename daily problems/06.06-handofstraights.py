# Alice has some number of cards and she wants to rearrange the cards into 
# groups so that each group is of size groupSize, 
# and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is 
# the value written on the ith card and an integer groupSize, 
# return true if she can rearrange the cards, or false otherwise.
import heapq

class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count ={}
        for n in hand:
            count[n] = 1 + count.get(n, 0) # add 1 to previous count value, if there isn't one return 0

        minH = list(count.keys())
        heapq.heapify(minH) # takes in an input array and transforms it into a minheap
        while minH:
            first = minH[0] # minimum value 

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1 # if the number is available, decrement the count by one
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        #if a value is always available in the minheap, then
        # the loop will exit, meaning you can just return True.
        # at any point during the loop if there is an eror, it will
        # already return False.
        return True
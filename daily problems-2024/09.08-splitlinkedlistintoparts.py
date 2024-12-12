# Given the head of a singly linked list and an integer k, 
# split the linked list into k consecutive linked list parts.

# The length of each part should be as equal as possible: 
# no two parts should have a size differing by more than one. 
# This may lead to some parts being null.

# The parts should be in the order of occurrence in the input list, 
# and parts occurring earlier should always have a size greater than 
# or equal to parts occurring later.

# Return an array of the k parts.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head, k: int):
        res = [None] * k
        other = head
        count = 0
        while other:
            count += 1
            other = other.next
        div_amount = count//k
        first_n = count % k

        cur = head
        for i in range(k):
            res[i] = cur
            cur_size = div_amount + (1 if first_n > 0 else 0)
            first_n -= 1

            for _ in range(cur_size - 1): # traversing to the end of the split size
                if cur:
                    cur = cur.next
            
            if cur:
                nex = cur.next
                cur.next = None
                cur = nex
        return res
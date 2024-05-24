 # Given the head of a linked list, 
# remove the nth node from the end of the list and 
# return its head.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head):
        dummy = ListNode(0, head) # next node is set to the head of the list
        left = dummy
        right = head

        # shift the right pointer n amount of times (right = left + n)
        while n > 0 and right:
            right = right.next
            n -= 1 # once n is 0, we have shifted n amount of times
        
        # actual pointer moving
        while right:
            left = left.next
            right = right.next

        # delete the nth node
        left.next = left.next.next
        return dummy.next
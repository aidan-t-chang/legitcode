# Given head, the head of a linked list, 
# determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in 
# the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer 
# is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        tortoise = head
        hare = head

        while hare and hare.next: # while the rightmost pointer does not encounter a null value
            tortoise = tortoise.next # shift by 1
            hare = hare.next.next # shift by 2

            if tortoise == hare:
                return True

        return False
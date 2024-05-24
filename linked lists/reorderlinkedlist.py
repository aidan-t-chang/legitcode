# You are given the head of a singly linked-list.

# The positions of a linked list of length = 7 for example, can intially be represented as:

# [0, 1, 2, 3, 4, 5, 6]

# Reorder the nodes of the linked list to be in the following order:

# [0, 6, 1, 5, 2, 4, 3]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # second half of the list
        prev = slow.next = None # splitting the second list and setting last value in first half to null value

        #reverse second portion of the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp # second is the next node in the list

        #merge two halves

        first, second = head, prev # second is set to null, but previous is set to the last node we looked at
        while second:
            temp1, temp2 = first.next, second.next # modify first and second half links
            first.next = second
            second.next = temp1 # inserting second node between first and first.next (temp1)
            first, second = temp1, temp2 # shift pointers
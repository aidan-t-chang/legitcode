# You are given an array of integers nums and the head of a linked list. 
# Return the head of the modified linked list after removing all nodes from 
# the linked list that have a value that exists in nums.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


        
class Solution:
    def modifiedList(self, nums, head):
        s = set(nums)

        while head and head.val in s:
            head = head.next

        if not head:
            return None
        
        l, r = head, head.next

        while r:
            if r.val not in s:
                l.next = r
                l = r
            r = r.next
        
        l.next = None
        return head
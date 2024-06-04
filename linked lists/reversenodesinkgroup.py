# Given the head of a linked list, 
# reverse the nodes of the list k at a time, 
# and return the modified list.

# k is a positive integer and is less than or 
# equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes, 
# in the end, should remain as it is.

# You may not alter the values in the list's nodes, 
# only nodes themselves may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        previous = dummy 

        while True:
            kth = self.getKth(previous, k)
            if not kth: # if it is null:
                break
            #keep track of node right after group
            groupNext = kth.next

            #reverse the group
            prev, curr = kth.next, previous.next
            while curr != groupNext:
                tem = curr.next
                curr.next = prev
                prev = curr
                curr = tem

            tem = previous.next # first node in the group
            previous.next = kth # putting kth at the beginning of the group
            previous = tem
        return dummy.next
    
    #shift k times and get the kth node
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
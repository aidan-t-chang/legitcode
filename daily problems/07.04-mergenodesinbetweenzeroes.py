# You are given the head of a linked list, 
# which contains a series of integers separated by 0's. 
# The beginning and end of the linked list will have Node.val == 0.

# For every two consecutive 0's, 
# merge all the nodes lying in between them into a single 
# node whose value is the sum of all the merged nodes. 
# The modified list should not contain any 0's.

# Return the head of the modified linked list.

class Solution:
    def mergeNodes(self, head):
        left, right = head, head.next
        curr_sum = 0
        while right:
            if right.val == 0:
                left.val = curr_sum
                curr_sum = 0
                right = right.next
                left.next = right
                left = right
            else:
                curr_sum += right.val
                right = right.next
        return head
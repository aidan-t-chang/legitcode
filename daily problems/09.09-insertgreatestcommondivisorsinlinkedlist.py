# Given the head of a linked list head, in which each node contains an integer value.
# Between every pair of adjacent nodes, 
# insert a new node with a value equal to the greatest common divisor of them.

# Return the linked list after insertion.

# The greatest common divisor of two numbers is the largest positive integer 
# that evenly divides both numbers.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head):
        if not head or not head.next:
            return head

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        node1 = head
        while node1.next:
            node2 = node1.next
            gcd_value = gcd(node1.val, node2.val)
            gcd_node = ListNode(gcd_value)
            node1.next = gcd_node
            gcd_node.next = node2
            node1 = node2

        return head
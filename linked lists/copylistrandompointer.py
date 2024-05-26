
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        tocopy = {None : None} # in the edge case the next value is null need a null node by default

        # first pass: cloning the linked list nodes and adding to hashmap
        current = head
        while current:
            copy = Node(current.val)
            tocopy[current] = copy
            current = current.next

        # second pass: using the hashmap in pass one to set next and random pointers for the copied linked list
        current = head
        while current:
            copy = tocopy[current]
            copy.next = tocopy[current.next] # map the copy next to the original using the hashmap
            copy.random = tocopy[current.random] 
            current = current.next
        
        return tocopy[head]
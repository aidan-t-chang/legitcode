# Given a binary tree root and a linked list with head as the first node. 

# Return True if all the elements in the linked list starting from the head correspond 
# to some downward path connected in the binary tree otherwise return False.

# In this context downward path means a path that starts at some node and goes downwards.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head, root) -> bool:

        def dfs(head, point, root):
            if not point:
                return True
            if not root:
                return False

            if point.val == root.val: # move pointer if values match in bst
                point = point.next
            elif head.val == root.val: # new attempt if linked list and bst values match
                head = head.next
            else:
                point = head
            
            return dfs(head, point, root.left) or dfs(head, point, root.right)
        return dfs(head, head, root)
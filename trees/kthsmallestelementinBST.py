# Given the root of a binary search tree, 
# and an integer k, return the kth smallest value (1-indexed) 
# of all the values of the nodes in the tree.

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
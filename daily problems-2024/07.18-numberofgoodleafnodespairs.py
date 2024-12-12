# You are given the root of a binary tree and an integer distance. 
# A pair of two different leaf nodes of a binary tree is said to be good if 
# the length of the shortest path between them is less than or equal to distance.

# Return the number of good leaf node pairs in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        def dfs(node) -> list[int]:
            if not node: return []
            if node.left is node.right:
                return [1]
            right = dfs(node.right)
            left = dfs(node.left)
            nonlocal res
            for r in right:
                for l in left:
                    if l + r <= distance:
                        res += 1
            leaves = []
            for x in right + left:
                x += 1
                if x < distance:
                    leaves.append(x)
            return leaves
        dfs(root)
        return res
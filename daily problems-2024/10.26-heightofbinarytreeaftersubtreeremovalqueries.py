# You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. 
# You are also given an array queries of size m.

# You have to perform m independent queries on the tree where in the ith query you do the following:

# Remove the subtree rooted at the node with the value queries[i] from the tree. 
# It is guaranteed that queries[i] will not be equal to the value of the root.
# Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

# Note:

# The queries are independent, so the tree returns to its initial state after each query.
# The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.


class Solution:
    def __init__(self):
        self.mp1 = {}
        self.mp2 = {}
        self.sz = {}
        self.id = 0
    
    def treeQueries(self, root, q):
        self.dfs(root, 0)
        left = [0] * self.id
        right = [0] * self.id
        
        for i in range(self.id):
            left[i] = self.mp2[i]
            if i > 0:
                left[i] = max(left[i - 1], left[i])
        
        for i in range(self.id - 1, -1, -1):
            right[i] = self.mp2[i]
            if i + 1 < self.id:
                right[i] = max(right[i], right[i + 1])
        
        ans = []
        for node in q:
            nodeid = self.mp1[node]
            l, r = nodeid, nodeid + self.sz[nodeid] - 1
            h = 0
            if l > 0:
                h = max(h, left[l - 1])
            if r + 1 < self.id:
                h = max(h, right[r + 1])
            ans.append(h)
        
        return ans
    
    def dfs(self, root, h: int) -> int:
        if not root:
            return 0
        self.mp1[root.val] = self.id
        self.mp2[self.id] = h
        self.id += 1
        lz = self.dfs(root.left, h + 1)
        rz = self.dfs(root.right, h + 1)
        self.sz[self.mp1[root.val]] = 1 + lz + rz
        return 1 + lz + rz
        
        

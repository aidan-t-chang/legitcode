# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization 
# algorithm should work. 
# You just need to ensure that a binary tree can be 
# serialized to a string and this string can be 
# deserialized to the original tree structure.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    #Encodes a tree to a single string.
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)     
        return ",".join(res)  
    # Decodes your encoded data to tree.
    def deserialize(self, data):
        vals = data.split(',') 
        self.i = 0 # global variable to use in dfs function

        def dfs():
            if vals[self.i] == "N": # node is null
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        

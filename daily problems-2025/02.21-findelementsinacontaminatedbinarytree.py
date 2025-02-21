# Given a binary tree with the following rules:

# root.val == 0
# For any treeNode:
# If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
# If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

# Implement the FindElements class:

# FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
# bool find(int target) Returns true if the target value exists in the recovered binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root):
        self.visit = set()
        root.val = 0
        def dfs(root):
            self.visit.add(root.val)
            if root.left:
                root.left.val = 2 * root.val + 1
                dfs(root.left)
            if root.right:
                root.right.val = 2 * root.val + 2
                dfs(root.right) 
        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.visit


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
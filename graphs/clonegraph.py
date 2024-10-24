# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        old = {}

        def dfs(node):
            if node in old:
                return old[node]

            copy = Node(node.val)
            old[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node) if node else None
        

            
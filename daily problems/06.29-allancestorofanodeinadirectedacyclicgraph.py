# You are given a positive integer n 
# representing the number of nodes of a Directed Acyclic Graph (DAG). 
# The nodes are numbered from 0 to n - 1 (inclusive).

# You are also given a 2D integer array edges, 
# where edges[i] = [fromi, toi] denotes that there is a 
# unidirectional edge from fromi to toi in the graph.

# Return a list answer, 
# where answer[i] is the list of ancestors of the ith node, 
# sorted in ascending order.

# A node u is an ancestor of another node v if u can reach v via a set of edges.


class Solution:
    def getAncestors(self, n, edges):
        res = [[] for _ in range(n)]
        direct = [[] for _ in range(n)]

        for edge in edges:
            direct[edge[0]].append(edge[1]) # the direct ancestor will be appended to the child
        for i in range(n):
            self.dfs(i, i, res, direct)
        return res
    def dfs(self, x, curr, res, direct):
        for child in direct[curr]:
            if not res[child] or res[child][-1] != x: 
                # if nested array for child does not exist or the nested array's last value is not i
                res[child].append(x) # append i to the ancestor list for the child
                self.dfs(x, child, res, direct) # recursive call
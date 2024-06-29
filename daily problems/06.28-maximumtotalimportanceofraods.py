# You are given an integer n denoting the number of cities in a country. 
# The cities are numbered from 0 to n - 1.

# You are also given a 2D integer array roads where roads[i] = [ai, bi] 
# denotes that there exists a bidirectional road connecting cities ai and bi.

# You need to assign each city with an integer value from 1 to n, 
# where each value can only be used once. 
# The importance of a road is then defined as the sum of the values of the two cities it connects.

# Return the maximum total importance of all roads possible after assigning the values optimally.

from collections import defaultdict


class Solution:
    def maximumImportance(self, n, roads):
        edgecount = [0] * n 
        for n1, n2 in roads: # get the frequency of edges in roads
            edgecount[n1] += 1
            edgecount[n2] += 1
        
        res = 0
        label = 1
        for count in sorted(edgecount): # assign labels in increasing order
            res += label * count # multiply the assigned value of a node by the number of times it appeared
            label += 1 # increment the importance(label) of a node as the iteration through the count continues
        return res

print(mar(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))

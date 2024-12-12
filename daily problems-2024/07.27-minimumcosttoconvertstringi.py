# You are given two 0-indexed strings source and target, 
# both of length n and consisting of lowercase English letters. 
# You are also given two 0-indexed character arrays original and changed, 
# and an integer array cost, where cost[i] represents the cost of 
# changing the character original[i] to the character changed[i].

# You start with the string source. In one operation, 
# you can pick a character x from the string and change it to the character 
# y at a cost of z if there exists any index j such that c
# ost[j] == z, original[j] == x, and changed[j] == y.

# Return the minimum cost to convert the string source to the string 
# target using any number of operations. 
# If it is impossible to convert source to target, return -1.

# Note that there may exist indices i, j such that 
# original[j] == original[i] and changed[j] == changed[i].

from collections import defaultdict
from heapq import heappush, heappop
from math import inf

class Solution:
    def minimumCostFrom(self, sourceChar):
        bests = {}
        seenCost = defaultdict(lambda: inf)
        seenCost[sourceChar] = 0
        frontier = [(0, sourceChar)]
        while len(frontier) > 0:
            reachCost, current = heappop(frontier)
            if current in bests:
                continue
            bests[current] = reachCost
            for d, edgeCost in self.edges[current].items():
                totalCost = reachCost + edgeCost
                if totalCost < seenCost[d]:
                    heappush(frontier, (totalCost, d))
                    seenCost[d] = totalCost
        return bests
    def minimumCost(self, source: str, target: str, original, changed, cost):
        self.edges = defaultdict(lambda: {})
        for i in range(len(original)):
            s = original[i]
            d = changed[i]
            c = cost[i]
            if d not in self.edges[s] or c < self.edges[s][d]:
                self.edges[s][d] = c

        bests = defaultdict(lambda: {})
        totalCost = 0
        for s, t in zip(source, target):
            if s != t:
                if t in bests[s]:
                    totalCost += bests[s][t]
                elif len(bests[s]) > 0:
                    return -1
                else:
                    best = self.minimumCostFrom(s)
                    bests[s] = best
                    if t in best:
                        totalCost += best[t]
                    else:
                        return -1
        return totalCost
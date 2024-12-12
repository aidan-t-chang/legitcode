# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] 
# represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most 
# distanceThreshold, If there are multiple such cities, return the city with the greatest number.

# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.



class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold):
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Distance to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Populate the distance matrix with the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Find the city with the smallest number of reachable cities
        # and if there is a tie, choose the city with the greatest number.
        minReachableCities = float('inf')
        bestCity = -1
        
        for i in range(n):
            reachableCities = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    reachableCities += 1
            
            if reachableCities <= minReachableCities:
                minReachableCities = reachableCities
                bestCity = i
        
        return bestCity
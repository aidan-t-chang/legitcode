# You are given a positive integer k. You are also given:

# a 2D integer array rowConditions of size n where 
# rowConditions[i] = [abovei, belowi], and
# a 2D integer array colConditions of size m where 
# colConditions[i] = [lefti, righti].
# The two arrays contain integers from 1 to k.

# You have to build a k x k matrix that contains each of the 
# numbers from 1 to k exactly once. The remaining cells should have the value 0.

# The matrix should also satisfy the following conditions:

# The number abovei should appear in a row that is strictly above
# the row at which the number belowi appears for all i from 0 to n - 1.
# the number lefti should appear in a column that is strictly
# left of the column at which the number righti appears for all i from 0 to m - 1.
# Return any matrix that satisfies the conditions. 
# If no answer exists, return an empty matrix.

from collections import defaultdict


class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        # return True if all okay and return False if cycle was found
        def dfs(src, graph, visited, cur_path, res) -> bool:
            if src in cur_path:
                return False  # cycle detected

            if src in visited:
                return True  # all okay, but we've already visited this node

            visited.add(src)
            cur_path.add(src)

            for neighbor in graph[src]:
                if not dfs(neighbor, graph, visited, cur_path, res):  # if any child returns false
                    return False

            cur_path.remove(src)  # backtrack path
            res.append(src)
            return True

        # if there will be cycle - return empty array, in other case return 1d array as described above
        def topo_sort(edges) -> list[int]:
            graph = defaultdict(list)
            for src, dst in edges:
                graph[src].append(dst)

            visited: set[int] = set()
            cur_path: set[int] = set()
            res: list[int] = []

            for src in range(1, k + 1, 1):
                if not dfs(src, graph, visited, cur_path, res):
                    return []

            return res[::-1]  # we will have res as reversed so we need to reverse it one more time

        row_sorting: list[int] = topo_sort(rowConditions)
        col_sorting: list[int] = topo_sort(colConditions)
        if [] in (row_sorting, col_sorting):
            return []

        value_position: dict[int, list[int]] = {
            n: [0, 0] for n in range(1, k + 1, 1)
        }  # element -> [row_index, col_index]
        for ind, val in enumerate(row_sorting):
            value_position[val][0] = ind
        for ind, val in enumerate(col_sorting):
            value_position[val][1] = ind

        res: list[list[int]] = [[0 for _ in range(k)] for _ in range(k)]
        for value in range(1, k + 1, 1):
            row, column = value_position[value]
            res[row][column] = value

        return res
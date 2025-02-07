# You are given an integer limit and a 2D array queries of size n x 2.

# There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. 
# For every query in queries that is of the form [x, y], you mark ball x with the color y. 
# After each query, you need to find the number of distinct colors among the balls.

# Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

# Note that when answering a query, lack of a color will not be considered as a color.

class Solution:
    def queryResults(self, limit: int, queries):
        res = []
        color = {}
        balls = {}

        for i in range(len(queries)):
            x, y = queries[i]
            if x in balls:
                prev = balls[x]
                color[prev] -= 1

                if not color[prev]:
                    del color[prev]

            balls[x] = y
            color[y] = color.get(y, 0) + 1
            res.append(len(color))

        return res
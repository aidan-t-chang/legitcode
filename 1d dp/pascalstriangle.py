# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int):
        dp = [[1]]

        nxt = [1]


        for j in range(numRows-1):
            for i in range(len(dp[-1])-1):
                nxt.append(dp[-1][i] + dp[-1][i+1])
            nxt.append(1)
            dp.append(nxt)
            nxt = [1]

        return dp
        
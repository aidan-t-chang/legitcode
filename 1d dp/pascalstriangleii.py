# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def getRow(self, rowIndex: int):
        dp = [[1]]
        for row in range(rowIndex):
            new = [1]
            for i in range(1, len(dp[-1])):
                new.append(dp[-1][i-1]+dp[-1][i])
            new.append(1)
            dp.append(new)
        return dp[-1]

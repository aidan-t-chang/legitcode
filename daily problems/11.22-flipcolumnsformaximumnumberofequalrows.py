# You are given an m x n binary matrix matrix.

# You can choose any number of columns in the matrix and flip every cell in that column 
# (i.e., Change the value of the cell from 0 to 1 or vice versa).

# Return the maximum number of rows that have all values equal after some number of flips.
from collections import defaultdict


class Solution:
    def maxEqualRowsAfterFlips(self, matrix) -> int:
        count = defaultdict(int)

        for row in matrix:
            rowk = tuple(row)

            if row[0]:
                rowk = tuple([0 if n else 1 for n in row])
            count[rowk] += 1

        return max(count.values())
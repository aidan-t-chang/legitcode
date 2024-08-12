# You start at the cell (rStart, cStart) of an rows x cols grid facing east. 
# The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

# You will walk in a clockwise spiral shape to visit every position in this grid. 
# Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). 
# Eventually, we reach all rows * cols spaces of the grid.

# Return an array of coordinates representing the positions of the grid in the order you visited them.


class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        i,j = rStart, cStart

        diri, dirj = 0, 1 # directions to move
        twice = 2
        res = []
        moves = 1
        next_moves = 2

        while len(res) < (rows * cols):
            if (-1 < i < rows) and ( -1 < j < cols):
                res.append([i,j])
            
            i += diri
            j += dirj
            moves -= 1
            if moves == 0:
                diri, dirj = dirj, -diri # 90 deg Clockwise
                twice -= 1
                if twice == 0:
                    twice = 2
                    moves = next_moves
                    next_moves += 1
                else:
                    moves = next_moves - 1
        return res
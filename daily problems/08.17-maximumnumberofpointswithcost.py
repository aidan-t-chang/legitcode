# You are given an m x n integer matrix points (0-indexed). 
# Starting with 0 points, 
# you want to maximize the number of points you can get from the matrix.

# To gain points, you must pick one cell in each row. 
# Picking the cell at coordinates (r, c) will add points[r][c] to your score.

# However, you will lose points if you pick a cell too far from the cell 
# that you picked in the previous row. 
# For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), 
# picking cells at coordinates (r, c1) and (r + 1, c2) will subtract 
# abs(c1 - c2) from your score.

# Return the maximum number of points you can achieve.


class Solution:
    def maxPoints(self, points) -> int:
        m, n = len(points), len(points[0])
        prev = points[0]
        
        for r in range(1, m):
            left = [0] * n
            right = [0] * n
            
            # Compute left max array
            left[0] = prev[0]
            for c in range(1, n):
                left[c] = max(left[c-1], prev[c] + c)
            
            # Compute right max array
            right[-1] = prev[-1] - (n-1)
            for c in range(n-2, -1, -1):
                right[c] = max(right[c+1], prev[c] - c)
            
            # Update current row using left and right arrays
            for c in range(n):
                prev[c] = points[r][c] + max(left[c] - c, right[c] + c)
        
        return max(prev)
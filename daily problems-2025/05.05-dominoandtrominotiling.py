""" You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile. """

class Solution:
    def numTilings(self, n: int) -> int:
        arr = [1, 2, 5]

        for i in range(3, n):
            arr.append(arr[i-1] * 2 + arr[i-3])
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        return arr[-1] % (10**9 + 7)
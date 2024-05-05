# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

def welcome(matrix, target):
    rows, columns = len(matrix), len(matrix[0])

    top, bot = 0, rows
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
    
    if not top <= bot:
        return False
    row = (top + bot) // 2
    l, r = 0, columns - 1
    while l <= r:
        middle = (l + r) // 2
        if target > matrix[row][middle]:
            l = middle + 1
        elif target < matrix[row][middle]:
            r = middle - 1
        else:
            return True
    return False


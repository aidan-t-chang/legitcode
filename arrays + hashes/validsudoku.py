# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

import collections

def isValid(board):
    columns = collections.defaultdict(set) # to check for duplicates in columns
    rows = collections.defaultdict(set) # to check for duplicates in rows
    squares = collections.defaultdict(set) # to check for duplicates in the 9 squares (r // 3, c // 3)

    for r in range(9): # there will be 9 rows every time in the board
        for c in range(9): # 9 columns every time in the board
            if board[r][c] == ".": # if the value is empty, just skip it
                continue
            if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r//3, c//3)]:
            # is the current value we are at (board[r][c]) already in the row number we are at, or in the columns, or if its in the squares?
                return False
            columns[c].add(board[r][c]) # add to our dictionary / hash map of our columns the current value we are at in order to search for duplicates next iteration
            rows[r].add(board[r][c]) # add to dictionary / hash map of rows the current value we are at
            squares[(r//3,c//3)].add(board[r][c]) # add to dictionary / hash map of squares the current value we are at  
    return True # if there is a duplicate, there is a 100% chance it would have returned False already.

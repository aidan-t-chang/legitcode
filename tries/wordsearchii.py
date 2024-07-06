# Given an m x n board of characters and a list of strings words, 
# return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once in a word.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.add_word(w)
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
            r == rows or c == cols or
            (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]] # we know that the node exists
            word += board[r][c]
            if node.isWord:
                res.add(word) # checking if the word is an actual word and is in words

            dfs(r-1, c, node, word) # change all the coordinates
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            visit.remove((r, c)) # actual backtracking

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)
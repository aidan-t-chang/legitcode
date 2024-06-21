# Implement the Trie class:

# Trie() Initializes the trie object.
# insert(String word) Inserts the string word into the trie.
# boolean search(String word) 
# Returns true if the string word is in the trie 
# (i.e., was inserted before), and false otherwise.

# boolean startsWith(String prefix) 
# Returns true if there is a previously inserted string word 
# that has the prefix prefix, and false otherwise.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class Trie:

    def __init__(self):
       self.root = TrieNode() 

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endofword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
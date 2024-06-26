# Design a data structure that supports adding new words and 
# searching for existing words.

# Implement the WordDictionary class:

# void addWord(word) Adds word to the data structure.
# bool search(word) Returns true if there is any 
# string in the data structure that matches word or false otherwise. 
# word may contain dots '.' where dots can be matched with any letter.

class TrieNode:
    def __init__(self):
        self.children = {} # a: TrieNode(a)
        self.word = False # tracks if something is the end of a word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] # if the char already exists, move to that char in case a new letter needs to be added
        cur.word = True # designated final letter as the end of the word  

    def search(self, word: str) -> bool:
        def dfs(j, root): # j: index parameter
                          # root: node operating on
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".": 
                # dot matches every character, so for each beginning char made right now
                # dfs through each one and see if a word ends at # of dots
                    for child in cur.children.values():
                        if dfs(i+1, child):#skipping the dot (i+1)
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)

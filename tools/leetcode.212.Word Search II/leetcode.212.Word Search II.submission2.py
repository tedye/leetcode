class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}

    
    class Trie:
        class TrieNode:
            # Initialize your data structure here.
            def __init__(self,key):
                self.key = key
                self.isWord = False
                self.next = {}
    
        def __init__(self):
            self.root = self.TrieNode('')
    
        # @param {string} word
        # @return {void}
        # Inserts a word into the trie.
        def insert(self, word):
            temp = self.root
            for i in word:
                if i not in temp.next:
                    temp.next[i] = self.TrieNode(i)
                temp = temp.next[i]
            temp.isWord = True
    
        # @param {string} word
        # @return {boolean}
        # Returns if the word is in the trie.
        def search(self, word):
            temp = self.root
            for i in word:
                if i not in temp.next:
                    return False
                temp = temp.next[i]
            return temp.isWord
    
        # @param {string} prefix
        # @return {boolean}
        # Returns if there is any word in the trie
        # that starts with the given prefix.
        def startsWith(self, prefix):
            temp = self.root
            for i in prefix:
                if i not in temp.next:
                    return False
                temp = temp.next[i]
            return True  
    
    def findWords(self, board, words):
        trie = self.Trie()
        for w in words:
            trie.insert(w)
        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.helper(board,trie.root,[[False] * (len(board[0])) for _ in range(len(board))], i, j, '', res)
        
        return list(res)
        
        
    def helper(self,  board, root, visited, x, y, cur,res):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or visited[x][y] or board[x][y] not in root.next:
            return
        
        c = board[x][y]
        cur += c
        if root.next[c].isWord:
            res.add(cur)
            
        visited[x][y] = True
        self.helper(board,root.next[c],visited,x-1,y,cur,res)
        self.helper(board,root.next[c],visited,x+1,y,cur,res)
        self.helper(board,root.next[c],visited,x,y-1,cur,res)
        self.helper(board,root.next[c],visited,x,y+1,cur,res)
        visited[x][y] = False
    
        
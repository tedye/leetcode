class WordDictionary:
    class Node:
        def __init__(self,c):
            self.key = c
            self.next = {}
            self.isWord = False
            
    def __init__(self):
        self.root = self.Node('')
        
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        i = 0
        l = len(word)
        temp = self.root
        while i < l and word[i] in temp.next:
            temp = temp.next[word[i]]
            i += 1
        if i != l:
            while i < l:
                temp.next[word[i]] = self.Node(word[i])
                temp = temp.next[word[i]]
                i += 1
        temp.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.helper(self.root, word)
        
    def helper(self,node,word):
        if not word: 
            return node.isWord
        i = 0
        l = len(word)
        if word[i] in node.next:
            return self.helper(node.next[word[i]],word[1:])
        elif word[i] == '.':
            flag = False
            for n in node.next.values():
                flag |= self.helper(n,word[1:])
            return flag
        else:
            return False
                    

        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
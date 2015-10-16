class TrieNode:
    # Initialize your data structure here.
    def __init__(self,key):
        self.key = key
        self.isWord = False
        self.next = {}

class Trie:

    def __init__(self):
        self.root = TrieNode('')

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        temp = self.root
        for i in word:
            if i not in temp.next:
                temp.next[i] = TrieNode(i)
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
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
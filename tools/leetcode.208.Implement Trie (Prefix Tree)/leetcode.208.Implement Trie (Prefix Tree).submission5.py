class TrieNode:
    # Initialize your data structure here.
    def __init__(self,key):
        self.key = key
        self.isWord = False
        self.next = [None] * 26

class Trie:

    def __init__(self):
        self.root = TrieNode('')

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        temp = self.root
        for i in word:
            if temp.next[ord(i)-ord('a')] == None:
                temp.next[ord(i)-ord('a')] = TrieNode(i)
            temp = temp.next[ord(i)-ord('a')]
        temp.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        temp = self.root
        for i in word:
            if temp.next[ord(i)-ord('a')] == None:
                return False
            temp = temp.next[ord(i)-ord('a')]
        return temp.isWord

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        temp = self.root
        for i in prefix:
            if temp.next[ord(i)-ord('a')] == None:
                return False
            temp = temp.next[ord(i)-ord('a')]
        return True      
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
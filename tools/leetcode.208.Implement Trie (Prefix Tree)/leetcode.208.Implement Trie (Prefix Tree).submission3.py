class TrieNode:
    # Initialize your data structure here.
    def __init__(self,c):
        self.key = c
        self.next = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode('')

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        temp = self.root
        for i in range(len(word)):
            if word[i] not in temp.next:
                temp.next[word[i]] = TrieNode(word[i])
            temp = temp.next[word[i]]
        temp.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        temp = self.root
        for i in range(len(word)):
            if word[i] not in temp.next:
                return False
            temp = temp.next[word[i]]
        return temp.isWord    

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        if not prefix: return True
        temp = self.root
        for i in range(len(prefix)):
            if prefix[i] not in temp.next:
                return False
            temp = temp.next[prefix[i]]
        return True       

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
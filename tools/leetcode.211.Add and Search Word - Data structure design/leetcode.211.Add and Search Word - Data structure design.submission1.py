class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.key = ''
        self.next = [None] * 26
        self.isWord = False

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        cur = word[0]
        if not self.next[ord(cur) - ord('a')]:
            self.next[ord(cur) - ord('a')] = WordDictionary()
        self.next[ord(cur) - ord('a')].key = cur
        if word[1:]:
            self.next[ord(cur) - ord('a')].addWord(word[1:])
        else:
            self.next[ord(cur) - ord('a')].isWord = True
            

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        if not word:
            return self.isWord
        cur = word[0]
        if cur == '.':
            for i in self.next:
                if i and i.search(word[1:]):
                    return True
            return False
        elif self.next[ord(cur) - ord('a')]:
            return self.next[ord(cur) - ord('a')].search(word[1:])
        else:
            return False
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.d = {}
        for i,word in enumerate(words):
            if word not in self.d:
                self.d[word] = [i]
            else:
                self.d[word].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.d[word1]
        l2 = self.d[word2]
        minDist = abs(l1[0] - l2[0])
        i,j = 0,0
        len1 = len(l1)
        len2 = len(l2)
        while i < len1 and j < len2:
            minDist = min(minDist, abs(l1[i] - l2[j]))
            if minDist == 1:
                break
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return minDist
            
        


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = {}
        d[word1] = -1
        d[word2] = -1
        minDist = 0x7fffffff
        for i,word in enumerate(words):
            if word == word1:
                d[word1] = i
                if d[word2] != -1:
                    minDist = min(minDist, i - d[word2])
            elif word == word2:
                d[word2] = i
                if d[word1] != -1:
                    minDist = min(minDist, i - d[word1])
        return minDist
                
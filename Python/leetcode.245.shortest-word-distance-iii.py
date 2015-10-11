please enter code here...
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            i = 0
            length = len(words)
            while i < length:
                if words[i] == word1:
                    break
                i += 1
            cur = i
            i += 1
            minDist = 0x7fffffff
            while i < length:
                if words[i] == word1:
                    minDist = min(minDist, i - cur)
                    cur = i
                i += 1
            return minDist
        
        
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
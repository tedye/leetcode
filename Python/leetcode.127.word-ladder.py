class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        # BFS
        scanLayer = [beginWord]
        distRecord = [1]
        while scanLayer:
            curWord = scanLayer.pop(0)
            dist = distRecord.pop(0)
            if curWord == endWord:
                return dist
            for i in range(len(beginWord)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = curWord[:i] + j + curWord[i+1:]
                    if newWord in wordList:
                        scanLayer.append(newWord)
                        distRecord.append(dist+1)
                        wordList.remove(newWord)
        return 0
class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
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
                    if newWord in wordDict:
                        scanLayer.append(newWord)
                        distRecord.append(dist+1)
                        wordDict.remove(newWord)
        return 0
        
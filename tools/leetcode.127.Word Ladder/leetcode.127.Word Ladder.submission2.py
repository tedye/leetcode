class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        if not wordDict: return 0
        
        wq = [beginWord]
        dq = [1]
        while wq:
            curw = wq.pop(0)
            dist = dq.pop(0)
            if curw == endWord:
                return dist
            for i in range(len(beginWord)):
                c = curw[i]
                for j in 'abcdefghihklmnopqrstuvwxyz':
                    neww = curw[:i] + j + curw[i+1:]
                    if neww in wordDict:
                        wq.append(neww)
                        dq.append(dist+1)
                        wordDict.remove(neww)
        return 0
                    
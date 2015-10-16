class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        if not wordDict: return 0
        
        q = []
        q.append((beginWord,1))
        while q:
            item = q.pop(0)
            curw = item[0]
            dist = item[1]
            if curw == endWord:
                return dist
            for i in range(len(beginWord)):
                c = curw[i]
                for j in 'abcdefghihklmnopqrstuvwxyz':
                    if j == c:
                        continue
                    neww = curw[:i] + j + curw[i+1:]
                    if neww in wordDict:
                        q.append((neww,dist+1))
                        wordDict.remove(neww)
        return 0
                    
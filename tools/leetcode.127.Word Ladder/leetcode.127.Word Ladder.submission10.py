class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, start, end, dict):
        dict.add(end)
        q = []
        q.append((start, 1))
        while q:
            curr = q.pop(0)
            currword = curr[0]; currlen = curr[1]
            if currword == end: return currlen
            for i in range(len(start)):
                part1 = currword[:i]; part2 = currword[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currword[i] != j:
                        nextword = part1 + j + part2
                        if nextword in dict:
                            q.append((nextword, currlen+1)); 
                            dict.remove(nextword)
        return 0
        
            
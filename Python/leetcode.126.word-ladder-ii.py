class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        result=[]
        prevMap={}
        length=len(beginWord)
        for i in wordlist:
            prevMap[i]=[]
        wordlist.add(beginWord)
        wordlist.add(endWord)
        candidates=[set(),set()]
        current=0; previous=1
        candidates[current].add(beginWord)
        while True:
            current, previous=previous, current
            for i in candidates[previous]: wordlist.remove(i)
            candidates[current].clear()
            for word in candidates[previous]:
                for i in range(length):
                    part1=word[:i]; part2=word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i]!=j:
                            nextword=part1+j+part2
                            if nextword in wordlist:
                                prevMap[nextword].append(word)
                                candidates[current].add(nextword)
            if len(candidates[current])==0: return []
            if endWord in candidates[current]: break
        self.buildpath([], endWord, result, prevMap)
        return result
        
    def buildpath(self, path, word, result, prevMap):
        if len(prevMap[word])==0:
            path.append(word)
            result.append(path[::-1])
            path.pop();
            return
        path.append(word)
        for iter in prevMap[word]:
            self.buildpath(path, iter,result, prevMap)
        path.pop()
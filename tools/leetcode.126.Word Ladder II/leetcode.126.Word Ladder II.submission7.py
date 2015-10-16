class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        result=[]
        prevMap={}
        length=len(start)
        for i in dict:
            prevMap[i]=[]
        candidates=[set(),set()]; current=0; previous=1
        candidates[current].add(start)
        while True:
            current, previous=previous, current
            for i in candidates[previous]: dict.remove(i)
            candidates[current].clear()
            for word in candidates[previous]:
                for i in range(length):
                    part1=word[:i]; part2=word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i]!=j:
                            nextword=part1+j+part2
                            if nextword in dict:
                                prevMap[nextword].append(word)
                                candidates[current].add(nextword)
            if len(candidates[current])==0: return []
            if end in candidates[current]: break
        self.buildpath([], end, result, prevMap)
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
    
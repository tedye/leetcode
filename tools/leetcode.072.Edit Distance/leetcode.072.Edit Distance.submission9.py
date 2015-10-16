class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        dist = [i for i in range(len(word1)+1)]
        cur = []
        for i in range(1,len(word2)+1):
            cur += [i]
            for j in range(1,len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    cur += [min(dist[j-1],cur[-1]+1,dist[j]+1)]
                else:
                    cur += [min(dist[j-1]+1,cur[-1]+1,dist[j]+1)]
            dist = cur[:]
            cur = []
        return dist[-1]

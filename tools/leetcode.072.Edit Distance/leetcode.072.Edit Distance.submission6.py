class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        dist = [i for i in range(len(word1)+1)]
        old = dist[0]
        for i in range(1,len(word2)+1):
            dist[0] = i
            for j in range(1,len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    temp = dist[j]
                    dist[j] = min(old,dist[j-1]+1,dist[j]+1)
                    old = temp
                else:
                    temp = dist[j]
                    dist[j] = min(old+1,dist[j-1]+1,dist[j]+1)
                    old = temp
            old = dist[0]

        return dist[-1]
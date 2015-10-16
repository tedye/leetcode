class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
            
    def canFinish(self, numCourses, prerequisites):
        l = len(prerequisites)
        if numCourses == 0 or l == 0:
            return True

        visit = [None] * numCourses

        d = {}
        start = set()
        for pair in prerequisites:
            if pair[1] in d:
                d[pair[1]].append(pair[0])
            else:
                d[pair[1]] = [pair[0]]
            start.add(pair[1])

        for i in start:
            if not self.helper(d,visit,i):
                return False
        return True

    def helper(self,d,visit,i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True

        visit[i] = -1
        if i in d:
            for j in d[i]:
                if not self.helper(d,visit,j):
                    return False

        visit[i] = 1
        return True
        
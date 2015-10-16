class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        adjlist = [set() for _ in range(numCourses)] 

        for p in prerequisites:
            adjlist[p[1]].add(p[0])

        indegrees = [0] * numCourses
        for i in range(numCourses):
            for x in adjlist[i]:
                indegrees[x] += 1
        q = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        res = []
        count = 0
        while q:
            cur = q.pop(0)
            for x in adjlist[cur]:
                indegrees[x] -= 1
                if indegrees[x] == 0:
                    q.append(x)

            res.append(cur)
            count += 1
        if count == numCourses:
            return res
        else:
            return []

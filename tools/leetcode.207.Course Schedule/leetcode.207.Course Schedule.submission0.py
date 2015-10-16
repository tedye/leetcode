class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses <2 or not prerequisites:
            return True
        
        indegree = {}
        outdegree = {}
        for i in range(numCourses):
            indegree[i] = 0
            outdegree[i] = []
        
        for pair in prerequisites:
            outdegree[pair[1]].append(pair[0])
            indegree[pair[0]] += 1
            
        visited = set()
        tovisit = [i for i in indegree if indegree[i] == 0 and i not in visited]
        while tovisit:
            for node in tovisit:
                visited.add(node)
                for n in outdegree[node]:
                        indegree[n] -= 1
            tovisit = [i for i in indegree if indegree[i] == 0 and i not in visited]
        return len(visited) == numCourses
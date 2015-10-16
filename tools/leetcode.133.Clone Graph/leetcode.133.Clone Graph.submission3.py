# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # BFS
        if not node:
            return None
        toVisit = set()
        visited = set()
        toVisit.add(node)
        while toVisit:
            tVisit = set()
            for x in toVisit:
                visited.add(x)
                for n in x.neighbors:
                    tVisit.add(n)       
            toVisit = tVisit - visited
        
        d = {}
        for x in visited:
            d[x] = UndirectedGraphNode(x.label)
        
        for x in visited:
            for n in x.neighbors:
                d[x].neighbors.append(d[n])
        return d[node]
        
        
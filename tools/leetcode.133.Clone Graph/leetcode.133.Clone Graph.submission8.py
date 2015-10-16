# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        toVisit = [node]
        visited = set()
        c = {}
        while toVisit:
            cur = toVisit.pop(0)
            if cur not in visited:
                c[cur] = UndirectedGraphNode(cur.label)
                visited.add(cur)
                toVisit += cur.neighbors
        for n in c.keys():
            for neighbor in n.neighbors:
                c[n].neighbors += [c[neighbor]]
        
        return c[node]
        
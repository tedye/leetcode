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
        
        visited = set()
        toVisit = [node]
        dummy = {}
        while toVisit:
            cur = toVisit.pop(0)
            if cur not in visited:
                dummy[cur] = UndirectedGraphNode(cur.label)
                visited.add(cur)
                toVisit += cur.neighbors
        for n in dummy.keys():
            for neighbor in n.neighbors:
                dummy[n].neighbors += [dummy[neighbor]]
                
        return dummy[node]
        
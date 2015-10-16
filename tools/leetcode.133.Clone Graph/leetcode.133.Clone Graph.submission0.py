# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
            
        visited = set()
        tovisit = set()
        tovisit.add(node)
        while tovisit:
            nextlvl = set()
            for n in tovisit:
                visited.add(n)
                for neib in n.neighbors:
                    nextlvl.add(neib)
            tovisit = nextlvl - visited
        
        d = {}
        for n in visited:
            d[n] = UndirectedGraphNode(n.label)
        
        for n in d:
            for neib in n.neighbors:
                d[n].neighbors += [d[neib]]
        
        return d[node]
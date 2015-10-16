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
        visited = {}
        while toVisit:
            cur = toVisit.pop(-1)
            visited[cur] = UndirectedGraphNode(cur.label)
            for i in cur.neighbors:
                if i not in visited:
                    toVisit.append(i)
        for n in visited:
            visited[n].neighbors = [visited[i] for i in n.neighbors]
        
        return visited[node]
        
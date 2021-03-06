class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        d = {}
        for i in range(n):
            d[i] = {}
        for e in edges:
            u,v = e
            d[u][v] = e 
            d[v][u] = e
        # BFS
        visited = set()
        visited.add(0)
        queue = [0]
        while queue:
            u = queue.pop(0)
            for v in d[u]:
                if v in visited:
                    return False
                else:
                    queue.append(v)
                    del d[v][u]
                    visited.add(v)
        return True
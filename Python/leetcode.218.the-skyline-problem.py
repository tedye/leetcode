class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from heapq import *
        skyline,i,l,workset = [],0,len(buildings),[]
        while i < l or workset:
            if not workset or i < l and workset[0][1] >= buildings[i][0]:
                x = buildings[i][0]
                while i < l and x == buildings[i][0]:
                    heappush(workset, (-buildings[i][2],buildings[i][1]))
                    i += 1
            else:
                x = workset[0][1]
                while workset and workset[0][1] <= x:
                    heappop(workset)
            height = len(workset) and -workset[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x,height],
        return skyline
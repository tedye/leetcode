from heapq import *
class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        skyline,i,l,wkset= [],0,len(buildings),[]
        while i < l or wkset:
            if not wkset or i < l and buildings[i][0] <= wkset[0][1]:
                x = buildings[i][0]
                while i < l and buildings[i][0] == x: 
                    heappush(wkset, (-buildings[i][2], buildings[i][1]))
                    i += 1
            else:
                x = wkset[0][1]
                while wkset and wkset[0][1] <= x: heappop(wkset)
            height = len(wkset) and -wkset[0][0]
            if not skyline or height != skyline[-1][1]: skyline += [x, height],
        return skyline
        
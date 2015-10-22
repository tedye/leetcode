class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # basically try to solve for median for 1D array twice
        vertical_list = []
        horizontal_list = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    vertical_list += i,
                    horizontal_list += j,
        horizontal_list.sort()
        v,h = self.solveFor1D(vertical_list), self.solveFor1D(horizontal_list)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    result += abs(v-i) + abs(h-j)
        return result
    
    def solveFor1D(self,l):
        length = len(l)
        return l[length//2]

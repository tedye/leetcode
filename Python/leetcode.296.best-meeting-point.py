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
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j]:
                    horizontal_list += j,
                    
        v,h = self.solveFor1D(vertical_list), self.solveFor1D(horizontal_list)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    result += abs(v-i) + abs(h-j)
        return result
    
    def solveFor1D(self,l):
        length = len(l)
        if length & 1:
            return l[length//2]
        left = l[length//2 -1]
        right= l[length//2]
        if sum([left-n for n in l[:length//2]]) > sum([n - right for n in l[length//2:]]):
            return left
        else:
            return right

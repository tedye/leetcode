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
        result = 0
        while len(vertical_list) > 1:
            result += vertical_list.pop(-1) - vertical_list.pop(0)
            result += horizontal_list.pop(-1) - horizontal_list.pop(0)
        return result
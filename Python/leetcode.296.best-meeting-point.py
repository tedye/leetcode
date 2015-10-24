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
        start,end = 0,len(horizontal_list)-1
        
        while end -start >= 1:
            result += vertical_list[end] - vertical_list[start]
            result += horizontal_list[end] - horizontal_list[start]
            end -= 1
            start += 1
        return result

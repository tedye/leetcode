class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.touch(grid, i,j,m,n)
        return count
    
    def touch(self,grid,i,j,m,n):
        if i == -1 or i == m or j == -1 or j == n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.touch(grid, i-1,j,m,n)
        self.touch(grid, i+1,j,m,n)
        self.touch(grid, i,j-1,m,n)
        self.touch(grid, i,j+1,m,n)
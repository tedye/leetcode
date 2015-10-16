class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        if n == 0: return 0
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.touch(grid,i,m,j,n)
        return res
        
    def touch(self,grid,i,m,j,n):
        grid[i][j] = '0'
        if i > 0 and grid[i-1][j] == '1':
            self.touch(grid,i-1,m,j,n)
        if i < m -1 and grid[i+1][j] == '1':
            self.touch(grid,i+1,m,j,n)
        if j > 0 and grid[i][j-1] == '1':
            self.touch(grid,i,m,j-1,n)
        if j < n -1 and grid[i][j+1] == '1':
            self.touch(grid,i,m,j+1,n)
        
class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
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
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        if i > 0: self.touch(grid, i-1,j,m,n)
        if i < m -1: self.touch(grid, i+1,j,m,n)
        if j > 0: self.touch(grid, i,j-1,m,n)
        if j < n -1: self.touch(grid, i,j+1,m,n)
        
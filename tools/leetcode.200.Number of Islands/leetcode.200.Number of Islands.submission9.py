class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if not grid or not grid[0]: return 0
        count = 0
        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    self.visit(grid,i,j,h,w)
                    count += 1
        return count
    
    def visit(self,grid,i,j,h,w):
        if i == -1 or i == h or j == -1 or j == w:
            return 
        
        if grid[i][j] == '1':
            grid[i][j] = 'x'
            self.visit(grid,i+1,j,h,w)
            self.visit(grid,i-1,j,h,w)
            self.visit(grid,i,j+1,h,w)
            self.visit(grid,i,j-1,h,w)
        
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid: return 0
        line = []
        M = len(grid)
        N = len(grid[0])
        for m in range(M):
            for n in range(N):
                if m == 0:
                    if n == 0:
                        line.append(grid[0][0])
                    else:
                        line.append(line[n-1] + grid[0][n])
                else:
                    if n == 0:
                        line[0] = grid[m][0]+line[0]
                    else:
                        line[n] = min(line[n] + grid[m][n], line[n-1] + grid[m][n])
        
        return line[-1]
        
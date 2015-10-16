class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) < 1: return 0
        if len(obstacleGrid) == 1:
            if obstacleGrid[0].count(1) != 0: return 0
            else: 
                print("here")
                return 1
        if len(obstacleGrid[0]) == 1:
            for i in obstacleGrid:
                if i[0] == 1:
                    return 0
            return 1
        dist = []
        flag = False
        for i in obstacleGrid[0]:
            if i == 0 and not flag:
                dist.append(1)
            else:
                dist.append(0)
                flag = True

        for i in range(1,len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dist[j] = 0
                    continue
                if j != 0:
                    dist[j] = dist[j]+ dist[j-1]

        return dist[-1]
        
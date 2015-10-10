class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        h = len(dungeon)
        w = len(dungeon[0])
        dp = [0x7fffffff] * (w+1)
        dp[-1] = dp[-2] = 1
        for i in range(w-1, -1, -1):
            dp[i] = max(min(dp[i], dp[i+1])-dungeon[-1][i],1)
        dp[-1] = 0x7fffffff
        for i in range(h-2, -1, -1):
            for j in range(w-1, -1, -1):
                dp[j] = max(min(dp[j], dp[j+1])-dungeon[i][j],1)
        return dp[0]
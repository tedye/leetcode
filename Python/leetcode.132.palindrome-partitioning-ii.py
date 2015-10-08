class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        l = len(s)
        # dp[i] minimum count of palindrom components
        dp = [l-i for i in range(l+1)]
        isP = [[False] * l for _ in range(l)]
        current = l - 1
        while current >= 0:
            temp = current
            while temp < l:
                if s[temp] == s[current] and (temp - current < 2 or isP[current+1][temp-1]):
                    isP[current][temp] = True
                    dp[current] = min(dp[current], dp[temp+1]+1)
                temp += 1
            current -= 1
        return dp[0] - 1
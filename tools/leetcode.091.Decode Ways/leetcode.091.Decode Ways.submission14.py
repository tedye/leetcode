class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s: return 0
        x = len(s)
        if x == 1: 
            if s == '0':
                return 0
            return 1
        dp = [0] *(x+1)
        if s[-1] == '0':
            dp[-2] = 0
        else:
            dp[-2] = 1
        dp[-1] = 1
        for i in range(1,x):
            con = int(s[x-1-i])
            if con == 0:
                dp[-2-i] = 0
            elif con == 1:
                dp[-2-i] = dp[-i]+dp[-1-i]
            elif con == 2:
                if 0 <= int(s[x-i]) <= 6:
                    dp[-2-i] = dp[-i]+dp[-1-i]
                else:
                    dp[-2-i] = dp[-1-i]
            else:
                dp[-2-i] = dp[-1-i]
        return dp[0]
        
        
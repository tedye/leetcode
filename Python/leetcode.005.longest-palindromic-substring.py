class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [0] * 2001
        new_string = '#'
        for c in s:
            new_string += c
            new_string += '#'
        i = 0
        l = len(new_string)
        rightbound = 0 # current maximum length palindrome rightbound index
        currentMax = 0 # length of wing - current maximum length palindrome
        currentMaxInd = 0 # current maximum length palindrome center
        while i < l:
            if i <= rightbound:
                dp[i] = min(rightbound - i, dp[currentMaxInd * 2 - i])
            while i - dp[i] > 0 and i + dp[i] < l-1 and new_string[i-dp[i]-1] == new_string[i+dp[i]+1]:
                dp[i] += 1
            if dp[i] > currentMax:
                currentMax = dp[i]
                currentMaxInd = i
                rightbound = i+dp[i]
            i += 1
        return ''.join(new_string[currentMaxInd-currentMax+1: currentMaxInd+currentMax].split('#'))
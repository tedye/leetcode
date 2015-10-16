class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s
        prefix = self.getPrefix(s+'#'+s[::-1])
        return s[prefix[-1]+1:][::-1] + s
        
    def getPrefix(self, s):
        prefix = [-1] * len(s)
        j = -1
        for i in range(1, len(s)):
            while j != -1 and s[j+1] != s[i]:
                j = prefix[j]
            if s[j+1] == s[i]:
                j += 1
            prefix[i] = j
        return prefix
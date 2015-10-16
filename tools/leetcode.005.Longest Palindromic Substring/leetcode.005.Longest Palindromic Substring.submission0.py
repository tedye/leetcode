class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if len(s) < 2: return s
        
        p = [0] * 2001
        s = ''.join([i+'#' for i in s]) + '#'
        i = 0
        l = len(s)
        MaxPos = 0
        rightb = 0
        while i < l:
            if i < rightb:
                p[i] = min(p[2*MaxPos - i], rightb-i)
            else:
                p[i] = 1
            while i-p[i] >= 0 and i+p[i] < l and s[i+p[i]] == s[i-p[i]]:
                p[i] += 1
            if p[i] > p[MaxPos]:
                MaxPos = i
                rightb = i+p[i]
            i += 1
        return ''.join(s[MaxPos-p[MaxPos]+1:MaxPos+p[MaxPos]].split('#'))
        
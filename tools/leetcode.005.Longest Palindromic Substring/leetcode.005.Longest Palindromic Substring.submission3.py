class Solution:    # @param {string} s    # @return {string}    def longestPalindrome(self, s):        if len(s) < 2: return s                ps = ''.join(['#'+i for i in s]+['#'])        p = [0] * 2001        MaxPos = 0        rightB = 0        for i in range(len(ps)):            if i < rightB:                p[i] = min(p[MaxPos*2-i], rightB-i)            else:                p[i] = 1                        while i-p[i] >= 0 and i+p[i] < len(ps) and ps[i+p[i]] == ps[i-p[i]]:                p[i] += 1                        if p[i] > p[MaxPos]:                MaxPos = i                rightB = i+p[i]        return ''.join(ps[MaxPos-p[MaxPos]+1:MaxPos+p[MaxPos]].split('#'))        
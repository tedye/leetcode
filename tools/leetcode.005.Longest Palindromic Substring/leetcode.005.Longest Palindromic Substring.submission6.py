class Solution:
    # @return a string
    def longestPalindrome(self, s):
        #use Manacher's algorithm
        p = [0] * 2001
        ns = '#'
        for e in s:
            ns += (e+'#')
        rightBound = 0
        maxPos = 0
        for i in range(len(ns)):
            if rightBound > i:
                p[i] = min(p[2*maxPos - i], rightBound - i)
            else:
                p[i] = 1
            while i-p[i] >= 0 and i + p[i] < len(ns) and ns[i+p[i]] == ns[i-p[i]]:
                p[i] += 1
            if p[i] > p[maxPos]:
                rightBound = i + p[i]
                maxPos = i

        maxstr = ns[maxPos-p[maxPos]+1:maxPos+p[maxPos]]
        return ''.join(maxstr.split('#'))
        
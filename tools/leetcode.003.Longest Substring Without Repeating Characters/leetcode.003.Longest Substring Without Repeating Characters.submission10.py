class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        l = len(s)
        if l < 2: return l
        
        i = 0
        cur = ''
        m = 0
        while i < l:
            if s[i] not in cur:
                cur += s[i]
            else:
                cur = cur[cur.index(s[i])+1:]+s[i]
            m = max(m,len(cur))
            i += 1
        return m
        
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        cur = ''
        m = 0
        
        for c in s:
            if c in cur:
                cur = cur[cur.index(c)+1:] + c
            else:
                cur += c
            m = max(m, len(cur))
        return m
            
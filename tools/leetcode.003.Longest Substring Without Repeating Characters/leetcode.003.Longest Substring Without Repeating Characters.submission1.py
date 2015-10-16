class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
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
            
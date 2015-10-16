class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if len(s) < 2: return len(s)
        
        start = 0
        end = 1
        length = len(s)
        ml = 1
        while end < length:
            if s[end] in s[start:end]:
                start += s[start:end].index(s[end])+1
            end+=1
            ml = max(ml,end-start)
        return ml
        
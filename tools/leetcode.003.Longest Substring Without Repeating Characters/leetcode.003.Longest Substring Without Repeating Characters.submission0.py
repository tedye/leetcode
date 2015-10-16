class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        result = 0
        start = 0
        end = 0
        for i in range(len(s)):
            end += 1
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
            d[s[i]] = i
            result = max(result, end - start)
        return result
            
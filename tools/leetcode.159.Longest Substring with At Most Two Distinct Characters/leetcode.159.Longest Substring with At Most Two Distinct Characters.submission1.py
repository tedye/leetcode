class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        startPos = 0
        limit = 2
        d = {}
        maxlen = 0
        for i, c in enumerate(s):
            if len(d) == limit and c not in d:
                rank = sorted([(d[j],j) for j in d])
                maxlen = max(maxlen, rank[-1][0] - startPos + 1)
                startPos = rank[0][0]+1
                del d[rank[0][1]]
            d[c] = i
        rank = sorted([(d[j],j) for j in d])
        return max(maxlen, rank[-1][0] - startPos + 1)
        
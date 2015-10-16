class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        if not strs:
            return res
        common = strs[0]
        for s in strs:
            i = 0
            while i < len(s) and i < len(common) and common[i] ==  s[i]:
                i +=1
            common = common[:i]
        return common
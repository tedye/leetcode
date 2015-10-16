class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        common = strs[0]
        for str in strs:
            cnt = 0
            while cnt != len(str) and cnt != len(common):
                if common[cnt] != str[cnt]: break
                cnt += 1
            common = common[:cnt]
        return common
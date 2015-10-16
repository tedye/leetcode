class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs or '' in strs:
            return ''
        common = strs[0]
        for s in strs[1:]:
            ind = 0
            l = min(len(common),len(s))
            while ind < l and common[ind] == s[ind]:
                ind += 1
            common = common[:ind]
        return common
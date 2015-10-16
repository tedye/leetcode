class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if needle == "": return 0
        if len(needle)> len(haystack):
            return -1
        startpos = 0
        l = len(needle)
        endpos = len(haystack) - len(needle)
        while startpos <= endpos:
            cur = 0
            while cur < l and needle[cur] == haystack[cur+startpos]:
                cur += 1
            if cur == l:
                return startpos
            else:
                startpos += 1
        return -1
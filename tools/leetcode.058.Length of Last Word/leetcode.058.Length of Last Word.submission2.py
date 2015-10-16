class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if not s: return 0
        l = s.strip().split(' ')
        if l:
            return len(l[-1])
        else:
            return 0
            
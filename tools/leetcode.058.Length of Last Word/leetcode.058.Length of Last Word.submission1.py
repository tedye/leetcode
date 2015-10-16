class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        temp = [w for w in s.split() if w]
        
        if temp:
            return len(temp[-1])
        else:
            return 0
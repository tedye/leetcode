class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        cnt = 0
        for c in s:
            cnt *= 26
            cnt +=  + ord(c)- ord('A') + 1
        return cnt
        
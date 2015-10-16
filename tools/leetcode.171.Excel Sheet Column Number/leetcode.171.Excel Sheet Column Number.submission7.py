class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        record = [ord(i)- ord('A') + 1 for i in s[::-1]]
        cnt = 0
        base = 26
        for c in record[1:]:
            cnt += c*base
            base *= 26
        return cnt +  record[0]
        
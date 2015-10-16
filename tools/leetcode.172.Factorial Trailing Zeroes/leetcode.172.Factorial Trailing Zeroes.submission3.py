class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        base = 5
        cnt = 0
        while n // base:
            cnt += n // base
            base *= 5
        return cnt
        
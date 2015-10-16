class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        cnt = 0
        while n > 0:
            n //= 5
            cnt += n
        return cnt
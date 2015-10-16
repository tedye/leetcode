class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        count = 0
        base = 5
        while n // base > 0:
            count += n // base
            base *= 5
        return count
            
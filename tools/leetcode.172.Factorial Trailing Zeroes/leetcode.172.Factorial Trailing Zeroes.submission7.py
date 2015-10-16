class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        cnt = 0
        while n > 4:
            cnt += n // 5
            n //= 5
        return cnt
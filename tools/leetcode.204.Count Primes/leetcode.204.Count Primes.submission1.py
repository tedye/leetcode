class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 1:
            return 0
        p = [1] * n
        for i in range(2,n):
            if p[i]:
                j = i * i
                while j < n:
                    p[j] = 0
                    j += i
            i += 1
        return sum(p)-2
        
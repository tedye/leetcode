class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0
        x = [1] * n
        x[0] = 0
        x[1] = 0
        x[2] = 1
        i = 2
        while i < n:
            if x[i]:
                j = i*i
                while j < n:
                    x[j] = 0
                    j += i
            i += 1
        return sum(x)
        
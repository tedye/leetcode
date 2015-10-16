class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        # attempt two
        if n < 2:
            return 0
        container = [True] * n
        container[0] = False
        container[1] = False
        current = 2
        length = n**(0.5)
        while current < length:
            if container[current]:
                for i in range(current+current, n, current):
                    container[i] = False
            current += 1
        return container.count(True)
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # solve with recursion
        result = []
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                q = n // i
                result += [[i, q]]
                for x in self.getFactors(q):
                    if x[0] >= i:
                        result += [i] + x,
        return result
        
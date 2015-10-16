class Solution:
    # @return a string
    def getPermutation(self, n, k):
        num = [chr(49+i) for i in range(n)]
        permutation = [1] * (n + 1)
        for p in range(len(permutation)-1):
            permutation[p+1] = permutation[p] * (p+1)
        k -= 1
        residual = []
        pos = n-1
        k %= permutation[-1]
        while k > 0:
            residual += [k // permutation[pos]]
            k %= permutation[pos]
            pos -= 1
        result = []
        while residual:
            result += [num[residual[0]]]
            del num[residual[0]]
            del residual[0]
        result += num
        return ''.join(result)
        
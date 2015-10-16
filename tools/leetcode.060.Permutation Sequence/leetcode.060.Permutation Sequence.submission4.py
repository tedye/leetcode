class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        base = 1
        a = []
        for i in range(1,n+1):
            base *= i
            a.append(base)
        b = []
        k -= 1
        for i in a[::-1]:
            b += [k // i]
            k %=i
        
        x = [str(i) for i in range(1,1+n)]
        res = ''
        for i in range(n-1):
            res += x[b[i+1]]
            del x[b[i+1]]
        res += x[-1]
        return res
            
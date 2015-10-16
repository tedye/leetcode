class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        if n == 1:
            return '1'
        base = 1
        k -= 1
        factorial = [1]
        for i in range(2, n):
            factorial.append(factorial[-1]*i)
        nums = [chr(ord('0')+i) for i in range(1,n+1)]
        res = ''
        while factorial:
            b = factorial.pop(-1)
            t = k // b
            res +=  nums.pop(t)
            k -= t * b
        res += nums[0]
        return ''.join(res)
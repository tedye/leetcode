class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, A):
        if not A: return 1
        
        i = 0
        l = len(A)
        while i < l:
            while 0 < A[i] <= l and A[A[i]-1] != A[i]:
                temp = A[A[i]-1]
                A[A[i]-1] = A[i]
                A[i] = temp
            i += 1
        i = 0
        while i < l:
            if A[i] != i+1:
                return i+1
            i += 1
        return l+1
        
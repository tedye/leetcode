class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 1: return A[0]
        globalMax = A[0]
        currentMax = 0
        for a in A:
            currentMax = max(a,a+currentMax)
            globalMax = max(currentMax,globalMax)
    
        return globalMax
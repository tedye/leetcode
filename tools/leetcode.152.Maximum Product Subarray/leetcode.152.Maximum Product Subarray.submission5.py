class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if not A: return 0
        if len(A) == 1: return A[0]
        
        curMax = A[0]
        curMin = A[0]
        res = A[0]
        
        for i in range(1,len(A)):
            temp = curMax
            pos = A[i]
            curMax = max(max(curMax * pos, curMin * pos),pos)
            curMin = min(min(temp * pos, curMin * pos),pos)
            res = max(res,curMax)
        return res

    
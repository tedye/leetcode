class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if len(A) < 3: return 0
        
        res = 0
        r = len(A)-1
        l = 0
        rH = A[r]
        lH = A[l]
        
        while r > l:
            if lH < rH:
                l+=1
                if A[l] < lH:
                    res += lH - A[l]
                else:
                    lH = A[l] 
            else:
                r -= 1
                if A[r] < rH:
                    res += rH - A[r]
                else:
                    rH = A[r]
        return res
                
                    
        
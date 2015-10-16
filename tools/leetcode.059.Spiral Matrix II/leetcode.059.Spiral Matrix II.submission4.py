class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0: return []
        
        
        l = 0
        lb = 0
        r = n
        
        u = 0
        ub = 0
        d = n
        line = [0] * n
        res = [line[:] for i in range(n)]
        cnt = 0
        while 1:
            if l == r-lb:
                break
            while l < r-lb:
                cnt+=1
                res[u][l] = cnt
                l+=1
            u += 1
            l -= 1
            
            if u == d-ub:
                break
            while u < d-ub:
                cnt+=1
                res[u][l] = cnt
                u += 1
            u -= 1
            l -= 1
            
            if l < lb:
                break
            
            while l >= lb:
                cnt+=1
                res[u][l] = cnt
                l -= 1
            l += 1
            u -= 1
            
            if u <= ub:
                break
            while u > ub:
                cnt+=1
                res[u][l] = cnt
                u -= 1
            u += 1
            l += 1
            lb += 1
            ub += 1
        return res
        
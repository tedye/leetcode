class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        res = [] 
        cur = ['.' * n for _ in range(n)]
        x = [(1<<n) - 1]
        self.helper(0,0,0,cur,0,res,x)
        return res
        
    def helper(self,row,ld,rd,cur,ind,res,x):
        if row != x[0]:
            pos = x[0] & (~(row|ld|rd))
            while pos:
                p = pos &(~pos+1)
                pos = pos-p
                self.setq(cur,ind,p,'Q')
                self.helper(row|p,(ld|p) << 1, (rd|p) >> 1,cur,ind+1,res,x)
                self.setq(cur,ind,p,'.')
        else:
            res.append(cur[:])
        
    def setq(self,cur,ind,p,c):
        col = 0
        while not (p&1):
            p >>= 1
            col += 1
        cur[ind] = cur[ind][:col] + c + cur[ind][col+1:]
        
                
        
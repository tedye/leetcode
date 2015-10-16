class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        cur = []
        res = []
        x = [i for i in range(1,10)]
        self.helper(x,res,cur,k,n,n)
        return res
        
    def helper(self,x,res,cur,level,target,n):
        if level == 0:
            if target == 0:
                res.append(cur[:])
                return
        if target > n:
            return
        for i in range(len(x)):
            cur.append(x[i])
            self.helper(x[i+1:],res,cur,level-1,target-x[i],n)
            cur.pop(-1)
            
            
            
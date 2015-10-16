class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        l = [i+1 for i in range(n)]
        
        cur = []
        res = []
        self.helper(l,res,cur,k)
        return res
    
    def helper(self, l, res, cur,k):
        if k == 0:
            res.append(cur[:])
            return
        for i,n in enumerate(l):
            cur.append(n)
            self.helper(l[i+1:],res,cur,k-1)
            cur.pop(-1)

        
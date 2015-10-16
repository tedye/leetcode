class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        if n < 0 or k < 0 or k > n: return []
        s = [i+1 for i in range(n)]
        cur = []
        res = []
        self.helper(s,res,cur,k)
        return res
    
    def helper(self,s,res,cur,k):
        if k == 0:
            res.append(cur[:])
            return 
        
        for i in range(len(s)):
            cur.append(s[i])
            self.helper(s[i+1:],res,cur,k-1)
            cur.pop(-1)
        
        
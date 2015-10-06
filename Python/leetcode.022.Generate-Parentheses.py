class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        l = r = n
        res = []
        cur = []
        self.helper(l,r,res,cur)
        return [''.join(i) for i in res]
    
    def helper(self,l,r,res,cur):
        if l == r == 0:
            res.append(cur[:])
            return
        
        if l > 0:
            cur.append('(')
            self.helper(l-1,r,res,cur)
            cur.pop(-1)
        if r > l:
            cur.append(')')
            self.helper(l,r-1,res,cur)
            cur.pop(-1)
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        d = {'0':'','1':' ','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        cur = []
        self.helper(digits,d,res,cur)
        return res
        
    def helper(self,digits,d,res,cur):
        if len(digits) == 0:
            res.append(''.join(cur))
            cur = []
            return
        
        for i in d[digits[0]]:
            cur += [i]
            self.helper(digits[1:],d,res,cur)
            del cur[-1]
    
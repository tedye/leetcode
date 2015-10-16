class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if not digits: return []
        if len(digits) == 1: return list(mapping[digits[0]])
        r = [mapping[i] for i in digits]
        return self.helper(r)
        
        
    def helper(self,r):
        if not r: return ['']
        prev = self.helper(r[1:])
        res = []
        for i in r[0]:
            res.extend([i+j for j in prev])
        return res
        
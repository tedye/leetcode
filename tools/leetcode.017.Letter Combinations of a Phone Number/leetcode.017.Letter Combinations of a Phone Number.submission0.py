class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        d = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7': 'pqrs', '8':'tuv', '9':'wxyz'}
        
        cur = []
        res = []
        self.helper(digits, res, cur, d)
        return res
        
    def helper(self, digits, res,cur,d):
        if not digits:
            res.append(''.join(cur))
            return
        
        c = digits[0]
        for j in d[c]:
            cur.append(j)
            self.helper(digits[1:],res,cur,d)
            cur.pop(-1)
class Solution:    # @param {integer[]} candidates    # @param {integer} target    # @return {integer[][]}    def combinationSum(self, candidates, target):        if not candidates: return []        res = []        cur = []        candidates.sort()        self.helper(candidates, target,res,cur)        return res            def helper(self, c, t, res, cur):        if t == 0:            res.append(cur[:])            return        if t < c[0]:            return         for num in c:            if num <= t:                if cur and cur[-1] > num:                    continue                cur.append(num)                self.helper(c, t-num, res,cur)                cur.pop(-1)            else:                break        
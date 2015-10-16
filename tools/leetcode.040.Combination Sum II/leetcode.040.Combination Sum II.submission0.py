class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: return []
        
        cur = []
        res = []
        d = {}
        for c in candidates:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        s = sorted(list(d.keys()))
        self.helper(s, d, target, cur, res)
        return res
        
    def helper(self, s, d, t, cur, res):
        if t == 0:
            res.append(cur[:])
            return
        
        for num in s:
            if num <= t:
                if cur and num < cur[-1] or d[num] == 0:
                    continue
                cur.append(num)
                d[num] -= 1
                self.helper(s, d, t-num, cur, res)
                cur.pop(-1)
                d[num] += 1
            else:
                break
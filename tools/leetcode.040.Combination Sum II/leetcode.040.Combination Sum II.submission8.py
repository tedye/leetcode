class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def __init__(self):
        self.res = []
        self.cur = []
        self.used = []
    
    def combinationSum2(self, candidates, target):
        if len(candidates) == 0: return []
        if len(candidates) == 1 and target == candidates[0]: return [candidates]
        candidates.sort()
        level = 0
        self.res = []
        self.cur = []
        self.used = []
        if target >= candidates[0]:
            self.helper(candidates,target,level)
        return self.res
        
    def helper(self, candidates,target,level):
        if target == 0:
            self.res.append(self.cur[:])
            return
        while level < len(candidates):
            temp = candidates[level]
            if candidates[level] <= target:
                self.cur.append(candidates[level])
                self.helper(candidates,target-candidates[level],level+1)
                del self.cur[-1]
                x = level
                while x + 1 < len(candidates) and temp == candidates[x + 1]:
                    level = x + 1
                    x+=1
            level += 1
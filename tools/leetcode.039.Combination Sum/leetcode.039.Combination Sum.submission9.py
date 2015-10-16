class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def __init__(self):
        self.cur = []
        self.res = []

    def combinationSum(self, candidates, target):
        if len(candidates) == 0: return []
        if len(candidates) == 1 and target == candidates[0]:
            return [candidates]
        self.cur = []
        self.res = []
        level = 0
        candidates.sort()
        if target >= candidates[0]:
            self.helper(candidates,target,level)
        return self.res
        
    def helper(self,candidates,target,level):
        if target == 0:
            self.res.append(self.cur[:])
            return

        for i in range(level,len(candidates)):
            if candidates[i] <= target:
                self.cur.append(candidates[i])
                self.helper(candidates,target-candidates[i],i)
                del self.cur[-1]
        
        
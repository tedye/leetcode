class Solution:
    # @return a tuple, (index1, index2)
    def threeSum(self, num):
        cur = []
        res = set()
        level = 0
        target = 0
        a = dict()
        r = []

        for i in num:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1

        self.helper(cur,res,a,target,level)  
        for e in res:
            r += [list(e)]

        return r


    def helper(self,cur,res,a,target,level):
        if level == 2:
            if target in a and a[target] > 0:
                t = tuple(sorted(cur+[target]))
                res.add(t)
            return

        for i in a:
            if a[i] > 0:
                cur += [i]
                a[i] -= 1
                target += -i
                self.helper(cur,res,a,target,level + 1)
                target -= -i
                a[i] += 1
                del cur[-1]
                    
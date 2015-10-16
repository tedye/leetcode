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

        for i in a:
            if a[i] > 0:
                cur += [i]
                a[i] -= 1
                for j in a:
                    if a[j] > 0:
                        cur += [j]
                        a[j] -= 1
                        target = -i-j
                        if target in a and a[target] > 0:
                            t = tuple(sorted(cur+[target]))
                            res.add(t)
                        a[j] += 1
                        del cur[-1]
                a[i] += 1
                del cur[-1]
        for e in res:
            r += [list(e)]

        return r
                    
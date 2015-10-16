class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if not S: return []
        S.sort()
        res = [[]]
        i = 0
        l = len(S)
        while i < l:
            next = []
            next.extend(res)
            for e in res:
                next.append(e+[S[i]])
            res = next
            i += 1
        return res
        
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        if len(S) == 1:
            return [[],S]
        S.sort()
        temp = self.subsetsWithDup(S[:-1])
        temp += [i+ [S[-1]] for i in temp if i+ [S[-1]] not in temp]
        return sorted(temp, key = len)

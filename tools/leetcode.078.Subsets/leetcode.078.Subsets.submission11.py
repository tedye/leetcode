class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if len(S) == 1:
            return [[],S]
        S.sort()
        temp = self.subsets(S[:-1])
        temp += ([i+ [S[-1]] for i in temp])
        return sorted(temp, key = len)
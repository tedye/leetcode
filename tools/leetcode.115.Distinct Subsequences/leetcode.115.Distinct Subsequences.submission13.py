class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if len(T) > len(S): return 0
        match = [0] * (len(T)+1)
        match[0] = 1
        i = 1
        while i <= len(S):
            j = len(T)
            while j > 0:
                if S[i-1] == T[j-1]:
                    match[j] += match[j-1]
                j -= 1
            i += 1
        return match[len(T)]
        
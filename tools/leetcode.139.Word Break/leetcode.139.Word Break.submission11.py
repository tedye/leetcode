class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        flags = [False] * (len(s)+1)
        flags[0] = True
        
        for i in range(len(s)):
            if not flags[i]:
                continue
            for d in wordDict:
                start = i
                end = start + len(d)
                if end > len(s):
                    continue
                if flags[end]:
                    continue
                if s[start:end] == d:
                    flags[end] = True
        return flags[-1]
                
class Solution:
    # @return a string
    def minWindow(self, S, T):
        if not S: return ''
        
        d = dict()
        s = set()
        for i in T:
            if i not in d:
                d[i] = 1
                s.add(i)
            else:
                d[i] += 1
        i = 0
        length = len(S)
        Min = 0
        res = ''
        curRightBoundary = 0
        while s and i < length:
            if S[i] in d:
                d[S[i]] -= 1
                if d[S[i]] == 0:
                    s.remove(S[i])
            i += 1
        if i == length and s:
            return ""
        while True:
            if S[curRightBoundary] not in d:
                curRightBoundary += 1
            elif d[S[curRightBoundary]] < 0:
                d[S[curRightBoundary]] += 1
                curRightBoundary += 1 
            else:
                break
        Min = i - curRightBoundary
        res = S[curRightBoundary:i]
        while i < length:
            if S[i] in d:
                d[S[i]] -= 1
            if S[curRightBoundary] == S[i]:
                while True:
                    if S[curRightBoundary] not in d: 
                        curRightBoundary += 1
                    elif d[S[curRightBoundary]] < 0:
                        d[S[curRightBoundary]] += 1
                        curRightBoundary += 1
                    else:
                        break
                if Min > i - curRightBoundary+1:
                    Min = i - curRightBoundary+1
                    res = S[curRightBoundary:i+1]

            i += 1

        return res
            
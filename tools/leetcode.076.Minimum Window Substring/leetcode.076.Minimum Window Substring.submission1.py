class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ''
        d = {}
        b = set()
        for i in t:
            if i not in d:
                d[i] = 1
                b.add(i)
            else:
                d[i] += 1
        # extend right side
        i = 0
        l = len(s)
        while i < l and b:
            if s[i] in d:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    b.remove(s[i])
            i += 1
        if i == l and b:
            return ''
        # shrink the left side
        lb = 0
        while lb < i:
            if s[lb] not in d:
                lb += 1
            elif d[s[lb]] < 0:
                d[s[lb]] += 1
                lb += 1
            else:
                break
        
        res = s[lb:i]
        while i < l:
            if s[i] in d:
                d[s[i]] -= 1
                if s[i] == s[lb]:
                    while lb < i:
                        if s[lb] not in d:
                            lb += 1
                        elif d[s[lb]] < 0:
                            d[s[lb]] += 1
                            lb += 1
                        else:
                            break
                    if len(res) > i - lb +1:
                        res = s[lb:i+1]
            i += 1
        return res
        
        
        
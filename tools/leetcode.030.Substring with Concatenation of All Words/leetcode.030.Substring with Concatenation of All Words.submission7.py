class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        width = len(words[0])*len(words)
        if not s or (len(s) < width): 
            return []
        if not s and len(words) == 1 and '' in words: 
            return [0]
        d = {}
        for i in words:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l = len(words)
        res = []
        w = len(words[0])
        for i in range(len(s) - width+1):
            temp = d.copy()
            if s[i:i+w] in temp:
                for j in range(l):
                    cur = s[i+j*w:i+w+j*w]
                    if cur in temp:
                        if temp[cur] > 0:
                            temp[cur] -= 1
                            if temp[cur] == 0:
                                del temp[cur]
                    else:
                        break
            if not temp:
                res.append(i)
        return res
            
        
        
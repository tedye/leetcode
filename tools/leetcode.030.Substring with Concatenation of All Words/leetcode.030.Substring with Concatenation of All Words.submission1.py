class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        c = len(words[0])
        width = c * len(words)
        if not words or not s or len(s) < width:
            return []
        
        d = {}
        for w in words:
            if w not in d:
                d[w] = 1
            else:
                d[w] += 1
        result = []
        for i in range(len(s) - width + 1):
            temp = d.copy()
            for j in range(i,i + width,c):
                wo = s[j:j+c]
                if wo in temp:
                    temp[wo] -= 1
                    if temp[wo] == 0:
                        del temp[wo]
                else:
                    break
            if not temp:
                result.append(i)
        return result
        
        
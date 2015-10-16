class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        d = {}
        for i in range(len(s)-9):
            w = s[i:i+10]
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        return [w for w in d if d[w] > 1]
        
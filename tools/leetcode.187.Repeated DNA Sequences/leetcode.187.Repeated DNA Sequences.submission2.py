class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        # use hashtable
        if len(s) < 10: return []
        d = {}
        for i in range(len(s) - 9):
            if s[i:i+10] in d:
                d[s[i:i+10]] += 1
            else:
                d[s[i:i+10]] = 1
        return [k for k in d if d[k] > 1]
        
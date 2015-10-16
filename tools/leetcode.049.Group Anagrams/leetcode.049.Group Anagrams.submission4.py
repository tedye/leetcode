class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        d = {}
        for s in strs:
            x = ''.join(sorted(list(s)))
            if x not in d:
                d[x] = [s]
            else:
                d[x].append(s)
        res = []
        for k in d:
            if len(d[k]) > 1:
                res.extend(d[k])
        return res
        
        
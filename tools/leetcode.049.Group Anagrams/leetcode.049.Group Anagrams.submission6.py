class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        d = {}
        for w in strs:
            t = ''.join(sorted(list(w)))
            if t not in d:
                d[t] = [w]
            else:
                d[t].append(w)
        res = []
        for k in d:
            if len(d[k]) > 1:
                res.extend(d[k])
        return res
        
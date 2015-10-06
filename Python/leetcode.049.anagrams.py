class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            x = ''.join(sorted(list(s)))
            if x not in d:
                d[x] = [s]
            else:
                d[x].append(s)
        res = []
        for k in d:
            res.append(sorted(d[k]))
        return res
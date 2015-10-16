class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ind0 = ind1 = pres = prep = 0
        lp = len(p)
        p += '#'
        isStart = False
        while ind0 < len(s):
            if s[ind0] == p[ind1] or p[ind1] == '?':
                ind0 += 1
                ind1 += 1
            elif p[ind1] == '*':
                while ind1 < lp and p[ind1] == '*':
                    ind1 += 1
                if ind1 == lp:
                    return True
                pres = ind0
                prep = ind1
                isStart = True
            elif isStart:
                pres += 1
                ind0 = pres
                ind1 = prep
            else:return False
        while ind1 < lp and p[ind1] == '*':
            ind1 += 1
        return lp == ind1
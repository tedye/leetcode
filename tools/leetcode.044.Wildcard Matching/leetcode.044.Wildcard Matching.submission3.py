class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        lp = len(p)
        p += '#'
        isStar = False
        pre_s = 0
        pre_p = 0
        index0 = index1 = 0
        while index0 < len(s):
            if s[index0] == p[index1] or p[index1] == '?':
                index1 += 1
                index0 += 1
            else:
                if p[index1] == '*':
                    while index1 < lp and p[index1] == '*':
                        index1 += 1
                    if index1 == lp:
                        return True
                    pre_s = index0 
                    pre_p = index1
                    isStar = True
                elif isStar:
                    pre_s += 1
                    index0 = pre_s
                    index1 = pre_p
                else: return False

        while index1 < lp and p[index1] == '*':
            index1 += 1
        return index1 == lp
        
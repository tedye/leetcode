class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # brute force way
        ls = len(s)
        lt = len(t)
        lenDiff = abs(lt-ls)
        if lenDiff > 1:
            return False
        elif lenDiff == 1:
            if ls > lt:
                templ = s
                temps = t
            else:
                templ = t
                temps = s
            headcount = 0
            for i in range(len(temps)):
                if temps[i] == templ[i]:
                    headcount += 1
                else:
                    break
            tailcount = 0
            for i in range(len(temps)):
                if temps[-i-1] == templ[-i-1]:
                    tailcount += 1
                else:
                    break
            return headcount+tailcount == len(temps)
        else:
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count += 1
            return count == 1
class Solution(object):    def isHappy(self, n):        """        :type n: int        :rtype: bool        """        if n == 1:            return True        if n == 4:            return False                x = sum([int(i) * int(i) for i in list(str(n))])        return self.isHappy(x)
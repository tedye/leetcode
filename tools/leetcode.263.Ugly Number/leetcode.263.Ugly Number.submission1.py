class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num == 0:
            return False
        while num & 3 == 0:
            num >>= 2
        while num & 1 == 0:
            num >>= 1
        while num % 15 == 0:
            num //= 15
        while num % 3 == 0 :
            num //= 3
        while num % 5 == 0:
            num //= 5
        return num == 1
        
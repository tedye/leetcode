class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        result = num % 9
        if result == 0:
            return 9
        else:
            return result
        
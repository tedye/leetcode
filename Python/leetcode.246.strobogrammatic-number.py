class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mapping = {'1':'1', '6':'9', '8':'8', '9':'6', '0':'0'}
        x = ''
        for n in num[::-1]:
            if n not in mapping:
                return False
            else:
                x += mapping[n]
        return x == num
        
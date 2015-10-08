class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str = str.strip()
        i = 0
        l = len(str)
        
        flag = False
        if str[i] == '-':
            flag = True
            i += 1
        elif str[i] == '+':
            i += 1
        
        result = 0
        while i < l and '0' <= str[i] <= '9':
            result = result * 10 + ord(str[i]) - ord('0')
            i += 1
        if not flag and result > 0x7fffffff:
            return 2147483647
        elif flag and result > 0x7fffffff+1:
            return -2147483648
        if flag:
            return -result
        else:
            return result

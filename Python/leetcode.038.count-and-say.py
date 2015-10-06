`class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ''
        if n == 1:
            return '1'
        
        prev = self.countAndSay(n-1)
        i = 0
        cur = prev[0]
        count = 0
        l = len(prev)
        res = ''
        while i < l:
            if prev[i] == cur:
                count += 1
                i += 1
            else:
                res += str(count) + cur
                cur = prev[i]
                count = 0
        res += str(count) + cur
        return res
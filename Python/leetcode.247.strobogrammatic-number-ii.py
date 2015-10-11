class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = [('0','0'),('1','1'),('6','9'),('8','8'),('9','6')]
        if n & 1:
            result = ['0','1','8']
        else:
            result = ['']
        if n < 2:
            return result

        for _ in xrange(n//2-1):
            temp = []
            for i in xrange(len(result)):
                for pair in l:
                    temp += [pair[0]+result[i]+pair[1]]
            result = temp
        temp = []
        for i in xrange(len(result)):
            for pair in l[1:]:
                temp += [pair[0]+result[i]+pair[1]]
        result = temp
                
                
        return result        
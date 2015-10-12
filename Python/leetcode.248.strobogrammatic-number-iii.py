class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if int(low) > int(high):
            return 0
        result = 0
        # count the numbers in between with different length than low and high
        for i in range(len(low)+1, len(high)):
            result += self.countlayer(i)

        lows = self.findStrobogrammatic(len(low))
        if len(low) == len(high):
            highs = lows
        else:
            highs = self.findStrobogrammatic(len(high))
        # do binary search to find the position
        i = 0
        j = len(lows)
        while i < j:
            mid = (i+j) // 2
            if lows[mid] > low:
                j = mid
            else:
                i = mid + 1
        
        k = 0
        l = len(highs)
        while k < l:
            mid = (k+l) // 2
            if highs[mid] > high:
                l = mid
            else:
                k = mid + 1
        if len(low) == len(high):
            result += k - i + 1
        else:
            result += len(lows) - i + k + + self.isStrobogrammatic(low)
        return result
        
    def countlayer(self,n):
        if n == 0:
            return 0
        if n&1:
            if n == 1:
                return 3
            else:
                return 12 * (5 **(n // 2 - 1))
        else:
            return 4 * (5 **(n // 2 - 1))
        
    
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
                
                
        return sorted(result)     
        
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
        
        
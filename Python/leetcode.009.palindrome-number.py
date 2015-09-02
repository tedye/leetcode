class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
            
        temp = x
        cnt = 0
        while temp:
            cnt += 1
            temp //= 10

        low = 0
        high = cnt - 1
        while low < high:
            if x % (10 ** (low+1)) // (10 ** low) != x % (10 ** (high+1)) // (10 ** high) :
                return False
            low += 1
            high -= 1
        return True

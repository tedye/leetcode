class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = [w for w in s.split() if w]
        
        if temp:
            return len(temp[-1])
        else:
            return 0
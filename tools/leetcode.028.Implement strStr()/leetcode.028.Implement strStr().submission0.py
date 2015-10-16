class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
        
        shift = computeShifts(needle)
    	startPos = 0
    	matchLen = 0
    	for c in haystack:
    		while matchLen >= 0 and needle[matchLen] != c:
    			startPos += shift[matchLen]
    			matchLen -= shift[matchLen]
    		matchLen += 1
    		if matchLen == len(needle):
    			return startPos
    			startPos += shift[matchLen]
    			matchLen -= shift[matchLen]
			
    def computeShifts(pattern):
    	shifts = [None] * (len(pattern) + 1)
    	shift = 1
    	for pos in range(len(pattern) + 1):
    		while shift < pos and pattern[pos-1] != pattern[pos-shift-1]:
    			shift += shifts[pos-shift-1]
    		shifts[pos] = shift
    	return shifts
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        
        a = ""
        currentL = 0
        MaxL = 0
        for letter in s:
            if letter not in a:
                a+=letter
                currentL += 1
                MaxL = max(currentL,MaxL)
            else:
                pos = a.find(letter)
                a = a[pos+1:]+letter
                currentL = len(a)
        return MaxL
class Solution:
    # @return a string
    def convertToTitle(self, num):
        l = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        if num // 26 == 0:
            return l[num%26]
        if num % 26 == 0:
            if num // 26 == 1:
                return 'Z'
            else:
                return self.convertToTitle(num // 26 - 1) + 'Z'
        else:
            return self.convertToTitle(num // 26) + self.convertToTitle(num % 26)
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        c = 0
        base = 1
        number = str(n)
        length = len(number)-1
        counter = [0]
        for i in range(length):
            counter.append(base + 10* c)
            c = counter[-1]
            base *= 10
        result = 0
        for i in range(length+1):
            if number[i] == '1':
                if number[i+1:]:
                    result += int(number[i+1:])+1 + counter[-1-i]
                else:
                    result += 1 + counter[-1-i]
            elif number[i] == '0':
                continue
            else:
                result += 10 ** (length - i) + int(number[i]) * counter[-1-i]
        return result
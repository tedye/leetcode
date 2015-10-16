class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        if not num: return ''
        res = []
        index = 0
        length = len(num)
        res += [str(num[index])]
        index += 1
        while index < len(num):
            t = str(num[index])
            i = 0
            l = len(res)
            while l>=i:
                mid = (i+l) >> 1
                if mid == len(res):
                    i = mid
                    break
                flag = self.compareTo(res[mid], t)
                if flag > 0:
                    i = mid+1
                elif flag < 0:
                    l = mid-1
                else: 
                    i = mid
                    break
            res = res[:i] + [t] + res[i:]
            index += 1
        res = ''.join(res)
        i = 0
        while i != len(res) - 1:
            if res[i] == '0':
                i += 1
            else:break
        return res[i:]

    def compareTo(self,s,t):
        if s[0] < t[0]:
            return -1
        elif s[0] > t[0]:
            return 1
        else:
            if len(s) == len(t):
                if len(s) == 1: return 0
                else: return self.compareTo(s[1:],t[1:]) 
            elif len(s) < len(t):
                i = 1

                while i < len(s):
                    if s[i] > t[i]:
                        return 1
                    elif s[i] < t[i]:
                        return -1
                    i += 1
                return self.compareTo(s,t[i:])
            else:
                i = 1
                while i < len(t):
                    if s[i] > t[i]:
                        return 1
                    elif s[i] < t[i]:
                        return -1
                    i += 1
                return self.compareTo(s[i:],t)
                
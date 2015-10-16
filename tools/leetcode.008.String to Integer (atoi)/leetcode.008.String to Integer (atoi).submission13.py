class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        if len(str) == 0: return 0
        sign = 1
        cnt = 0
        res = 0
        
        if str[0] == '-': 
            sign = -1
            cnt += 1
        elif str[0] == '+':
            cnt +=1
            
        overflow = False
        length = len(str)
        while cnt < length and not overflow:
            if str[cnt]<'0' or str[cnt] > '9' : break
            res = res * 10 + ord(str[cnt]) - ord('0')
            if res > 2147483647 and sign == 1:
                overflow = True
            elif res > 2147483648 and sign == -1:
                overflow = True
            cnt += 1
        
        if overflow:
            if sign == 1:
                return 2147483647
            else: return -2147483648
        else:
            return res * sign
        
        
        
        
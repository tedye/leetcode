class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1: return '1'
        res = '1.'
        for i in range(n-1):
            cnt = 0
            temp = ''
            common = res[0]
            for i in res:
                if common == i:
                    cnt +=1
                else:
                    temp += "{}".format(cnt)+common
                    cnt = 1
                    common = i
            res = temp+'.'
        return res[:-1]
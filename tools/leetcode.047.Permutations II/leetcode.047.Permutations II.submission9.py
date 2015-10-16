class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        res = [num]
        temp = self.nextPermu(num[:])
        while temp != num:
            res.append(temp)
            temp = self.nextPermu(temp[:])

        return res
    
    def nextPermu(self, num):
        s = 0
        e = len(num) - 2
        
        while e >= s:
            if num[e+1] <= num[e]: e -= 1
            else: break
        
        if e == -1:
            return num[::-1]
        if e == len(num) - 2:
            return num[:-2] + [num[-1],num[-2]]
        t = e + 1
        while t < len(num)-1:
            if num[t]>num[e]>=num[t+1]:
                break
            t+=1
        temp = num[t]
        num[t] = num[e]
        num[e] = temp
        
        return num[:e+1]+num[e+1:][::-1]
        
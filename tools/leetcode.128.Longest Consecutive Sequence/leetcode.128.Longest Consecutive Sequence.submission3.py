class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if not num: return 0
        if len(num) == 1: return 1
        
        visit = set(num)
        res = 0
        for i in num:
            temp = i
            cnt = 1
            while temp+1 in visit:
                cnt += 1
                temp = temp + 1
                visit.remove(temp)
            temp = i
            while temp-1 in visit:
                cnt += 1
                temp = temp - 1
                visit.remove(temp)
            res = max(cnt,res)
        return res
        
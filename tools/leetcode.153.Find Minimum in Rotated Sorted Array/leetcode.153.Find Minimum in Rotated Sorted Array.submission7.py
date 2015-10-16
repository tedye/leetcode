class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        # deal with the corner cases
        if len(num) == 0:
            return None
        if len(num) == 1:
            return num[0]
        if len(num) == 2:
            if num[0] >= num[1]:
                a = num[1]
                return num[1]
            else: return num[0]
        # num length greater than 2 i.e. at least 3
        if num[len(num)//2] >= max(num[0],num[-1]):
            return self.findMin(num[len(num)//2:len(num)])
        elif num[len(num)//2] <= min(num[0],num[-1]):
            return self.findMin(num[0:len(num)//2 + 1])
        else: return num[0]
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 0:return []
        if len(num) == 1:return [num]
        l = []
        self.permuteHelper(l,len(num),num)
        return l
    
    def permuteHelper(self,l,n,array):
        if n == 1: 
            l.append(array[:])
        else:
            for i in range(n):
                self.permuteHelper(l,n-1,array)
                if n % 2: j = 0
                else: j = i
                temp = array[j]
                array[j] = array[n-1]
                array[n-1] = temp
        
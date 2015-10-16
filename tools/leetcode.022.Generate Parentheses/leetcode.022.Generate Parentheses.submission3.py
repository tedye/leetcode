class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0: return [""]
        l = set()
        self.generateHelper(l,n,n,"")
        return list(l)

        
    def generateHelper(self,l,left,right,current):
        if left == right == 0: 
            l.add(current)
            return
        
        if left > 0:
            self.generateHelper(l,left-1,right,current+'(')
        if right > 0 and left < right:
            self.generateHelper(l,left,right-1,current+')')
        
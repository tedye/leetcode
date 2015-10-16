class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        tokens = self.tokenize(input)
        result = [tokens]
        while len(result[0]) > 1:
            n = []
            for i in result:
                for j in range(0,len(i)-2,2):
                    n += [i[:j]+['('+''.join(i[j:j+3])+')']+i[j+3:]]
            result = n
        return sorted(eval(j) for j in set([i[0] for i in result]))
    
    def tokenize(self, string):
        result = []
        i = 0
        l = len(string)
        cur = ''
        sign = {'+','-','*'}
        while i < l:
            if '0'<=string[i]<='9':
                cur += string[i]
            elif string[i] in sign:
                result += [cur]
                cur = ''
                result += [string[i]]
            i += 1
        if cur:
            result += [cur]
        return result
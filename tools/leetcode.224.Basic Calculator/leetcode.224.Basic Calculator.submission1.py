class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        if not s:
            return 0
        operS = []
        valueS = []
        tokens = self.tokenize(s)
        ops = {'+':1,'-':1,'*':2,'/':2}
        paren = {'(',')'}
        for token in tokens:
            if token not in ops and token not in paren:
                valueS.append(token)
            elif token == '(':
                operS.append(token)
            elif token == ')':
                while operS[-1] != '(':
                    op = operS.pop(-1)
                    op2 = valueS.pop(-1)
                    op1 = valueS.pop(-1)
                    res = 0
                    if op == '+':
                        res = op1 + op2
                    elif op == '-':
                        res = op1 - op2
                    elif op == '*':
                        res = op1 * op2
                    elif op == '/':
                        res = op1 // op2
                    valueS.append(res)
                operS.pop(-1)
            elif token in ops:
                while operS and operS[-1] in ops and ops[operS[-1]] >= ops[token]:
                    op = operS.pop(-1)
                    op2 = valueS.pop(-1)
                    op1 = valueS.pop(-1)
                    res = 0
                    if op == '+':
                        res = op1 + op2
                    elif op == '-':
                        res = op1 - op2
                    elif op == '*':
                        res = op1 * op2
                    elif op == '/':
                        res = op1 // op2
                    valueS.append(res)
                operS.append(token)
        while operS:
            op = operS.pop(-1)
            op2 = valueS.pop(-1)
            op1 = valueS.pop(-1)
            res = 0
            if op == '+':
                res = op1 + op2
            elif op == '-':
                res = op1 - op2
            elif op == '*':
                res = op1 * op2
            elif op == '/':
                res = op1 // op2
            valueS.append(res)    
        return valueS[0]
    
    def tokenize(self,s):
        i = 0
        l = len(s)
        ops = {'(',')','+','-','*','/'}
        result = []
        cur = ''
        while i < l:
            c = s[i]
            i += 1
            if c in ops:
                if cur:
                    result.append(int(cur))
                    cur = ''
                result.append(c)
            elif c == ' ':
                if cur:
                    result.append(int(cur))
                    cur = ''
                continue
            else:
                cur += c
        if cur:
            result.append(int(cur))
        return result
            
class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        s = []
        ops = {'+','-','*','/'}
        i = 0
        l = len(tokens)
        while i < l:
            op = tokens.pop(0)
            if op in ops:
                op2 = s.pop(-1)
                op1 = s.pop(-1)
                if op == '+': s.append(op1+op2)
                if op == '-': s.append(op1-op2)
                if op == '*': s.append(op1*op2)
                if op == '/':
                    if op1*op2<0:
                        s.append(-(abs(op1)//abs(op2)))
                    else:
                        s.append(op1//op2)
            else:
                s.append(int(op))
            i += 1
        return s[0]
        
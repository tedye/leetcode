class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        if not tokens: return 0
        ops = {'+','-','*','/'}
        if tokens[-1] not in ops:
            return int(tokens.pop(-1))
        op = tokens.pop(-1)
        op2 = self.evalRPN(tokens)
        op1 = self.evalRPN(tokens)
        if op == '+':
            return op1+op2
        elif op == '-':
            return op1-op2
        elif op == '*':
            return op1*op2
        elif op == '/':
            if op1*op2<0:
                return -(abs(op1)//abs(op2))
            else:
                return op1//op2
        
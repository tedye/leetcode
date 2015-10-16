class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        s = {'+','-','*','/'}
        i = 0
        l = len(tokens)
        while i < l:
            a = tokens[i]
            if a in s:
                op2 = stack.pop(-1)
                op1 = stack.pop(-1)
                if a == '+': stack += [op1 + op2]
                if a == '-': stack += [op1 - op2]
                if a == '*': stack += [op1 * op2]
                if a == '/': 
                    if op1 * op2 >= 0 or op1 % op2 == 0:
                        stack += [op1 // op2]
                    else:
                        stack += [op1 // op2 + 1]
            else:
                stack += [int(a)]
            i += 1
        return stack[0]
        
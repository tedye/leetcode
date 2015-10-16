class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        sign = {'+','-','*','/'}
        stack = []
        for i in tokens:
            if i in sign:
                op2 = stack.pop(-1)
                op1 = stack.pop(-1)
                if i == '/':
                    if (op1 > 0) ^ (op2 > 0):
                        stack.append(-(abs(op1) // abs(op2)))
                    else:
                        stack.append(op1//op2)
                elif i == '*':
                    stack.append(op1*op2)
                elif i == '+':
                    stack.append(op1+op2)
                elif i == '-':
                    stack.append(op1-op2)
            else:
                stack.append(int(i))
        return stack[0]
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        if not s: return 0
        
        stack = []
        for i in s:
            if not stack or i == '(':
                stack.append(i)
            elif i == ')':
                cur = str(eval(stack.pop(-1)+i))
                if stack:
                    stack[-1] += cur
                else:
                    stack.append(cur)
            else:
                stack[-1] += i
        return eval(stack[0])
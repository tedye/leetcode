class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        for item in s:
            if item == '(' or item == '[' or item == '{':
                stack.append(item)
            elif item == ')':
                if stack and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False
            elif item == ']':
                if  stack and  stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False
            elif item == '}':
                if  stack and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
        return stack == []
        
        
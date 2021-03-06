class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
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
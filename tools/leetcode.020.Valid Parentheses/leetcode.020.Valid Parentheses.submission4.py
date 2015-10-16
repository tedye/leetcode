class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = ['']
        for item in s:
            last = stack[-1]
            if last == '(' and item == ')' or last == '[' and item == ']' or last == '{' and item == '}':
                stack.pop(-1)
            else:
                stack.append(item)
        if len(stack) > 1:
            return False
        else:
            return True
            
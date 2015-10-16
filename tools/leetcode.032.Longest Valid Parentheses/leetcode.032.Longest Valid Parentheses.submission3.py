class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if not s: return 0
        stack = []
        left = [-1]
        i = 0
        l = len(s)-1
        res = 0
        while i <= l:
            if s[i] == '(':
                stack.append('(')
                left.append(i)
                i += 1
            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop(-1)
                    left.pop(-1)
                    res = max(res, i-left[-1])
                else:
                    stack.append(')')
                    left.append(i)
                i += 1
        return res
            
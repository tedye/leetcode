class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if not s:
            return 0
        stack = []
        left = [-1]
        i = 0
        l = len(s)
        result = 0
        while i < l:
            if s[i] == '(':
                stack.append(s[i])
                left.append(i)
            else:
                if stack and stack[-1] == '(':
                    stack.pop(-1)
                    left.pop(-1)
                    result = max(result, i - left[-1])
                else:
                    stack.append(s[i])
                    left.append(i)
            i += 1
        return result
        
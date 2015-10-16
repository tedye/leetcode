class Solution:    # @param s, a string    # @return an integer    def longestValidParentheses(self, s):        Max = 0        i = 0        length = len(s)        stack = []        while i != length:            if s[i] == '(':                stack.append(i)            else:                if stack and s[stack[-1]] == '(':                    stack.pop(-1)                    if stack:                        Max = max(Max,i - stack[-1])                    else:                        Max = max(Max, i+1)                else:                    stack.append(i)            i += 1        return Max
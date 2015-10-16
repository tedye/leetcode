class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        if not s:
            return 0
        stack = []
        for i in s:
            if i == ' ':
                continue
            if not stack and i != '(':
                stack.append(i)
            elif i == '(':
                stack.append('')
            elif i == ')':
                res = str(self.helper(stack.pop(-1)))
                if stack:
                    stack[-1]+= res
                else:
                    stack.append(res)
            else:
                stack[-1] += i
        return self.helper(stack.pop(0))
    
    def helper(self, s):
        op = {'-','+'}
        res = 0
        i = 0
        s = s
        l = len(s)
        number = ''
        while i < l:
            cur = 1
            while i < l and s[i] in op:
                if s[i] == '+':
                    cur = cur
                else:
                    cur = -cur
                i += 1
            while i < l and s[i] not in op:
                number += s[i]
                i += 1
            res += cur * int(number)
            number = ''
        return res
            
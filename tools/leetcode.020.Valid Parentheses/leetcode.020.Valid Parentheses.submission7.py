class Solution:
    # @return a boolean
    def isValid(self, s):
        if not s: return True
        if len(s)%2:return False
        stack = []
        right = ['(','[','{']
        left = [')',']','}']
        for i in s:
            if i in right:
                stack.append(i)
            elif i in left:
                if not stack: return False
                if right[left.index(i)] != stack[-1]:
                    return False
                else:
                    del stack[-1]
        if not stack:
            return True
        else:return False
    
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        p = [i for i in path.split('/') if i != '']
        for i in p:
            if i == '..':
                if stack:
                    del stack[-1]
            elif i != '.':
                stack += [i]
        if not stack:
            return '/'
        res = ''
        for i in stack:
            res += '/'+ i
        return res
        
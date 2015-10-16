class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        p = path.split('/')
        stack = []
        for token in p:
            if not token or token == '.' or token == '..' and not stack:
                continue
            elif token == '..':
                stack.pop(-1)
            else:
                stack.append(token)
        return '/'+'/'.join(stack)
        
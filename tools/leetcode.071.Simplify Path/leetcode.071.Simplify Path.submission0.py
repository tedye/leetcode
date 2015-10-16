class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
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
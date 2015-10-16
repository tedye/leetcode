class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        if not path: return ''
        p = [x for x in path.split('/') if x]
        s = []
        for n in p:
            if n == '..':
                if s:
                    s.pop(-1)
            elif n ==  '.':
                continue
            else:
                s.append(n)
        
        res = '/'.join(s)
        return '/'+res
        
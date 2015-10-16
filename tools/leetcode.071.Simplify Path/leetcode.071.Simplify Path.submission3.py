class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        l = path.split('/')
        cur = []
        for i in l:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if cur:
                    cur.pop(-1)
            else:
                cur.append(i)
        return '/' + '/'.join(cur)
        
                
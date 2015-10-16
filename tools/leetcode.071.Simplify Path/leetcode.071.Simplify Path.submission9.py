class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        root = self.node('')
        root.previous = root
        p = [i for i in path.split('/') if i != '']
        temp = root
        for i in p:
            if i == '..':
                temp = temp.previous
                temp.next = None
            elif i != '.':
                temp.next = self.node(i)
                temp.next.previous = temp
                temp = temp.next
        temp = root.next
        res = ''
        while temp != None:
            res += '/'+temp.val
            temp = temp.next
        if not res:
            return '/'
        return res

    class node:
        def __init__(self,x):
            self.val = x
            self.previous = None
            self.next = None
        
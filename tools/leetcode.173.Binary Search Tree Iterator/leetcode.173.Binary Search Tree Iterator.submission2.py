# Definition for a  binary tree node# class TreeNode:#     def __init__(self, x):#         self.val = x#         self.left = None#         self.right = Noneclass BSTIterator:    # @param root, a binary search tree's root node    def __init__(self, root):        self.index = 0        self.inorder = []        path = [root]        while path:            cur = path[-1]            if cur:                path.append(cur.left)            else:                path.pop(-1)                if path:                    cur = path.pop(-1)                    self.inorder.append(cur.val)                    path.append(cur.right)                self.length = len(self.inorder)                    # @return a boolean, whether we have a next smallest number    def hasNext(self):        return self.index < self.length    # @return an integer, the next smallest number    def next(self):        if self.index < self.length:            res = self.inorder[self.index]            self.index += 1            return res        # Your BSTIterator will be called like this:# i, v = BSTIterator(root), []# while i.hasNext(): v.append(i.next())
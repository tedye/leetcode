# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.flag = True
        if not root:
            self.flag = False
        else:
            self.root = root
            self.path = [root]
            self.current = root
            self.maximum = root.val

            temp = root
            while temp:
                if temp.left:
                    self.path.append(temp.left)
                    self.current = temp.left
                temp = temp.left
            temp = root
            while temp:
                if temp.right:
                    self.maximum = temp.right.val
                temp = temp.right

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.flag and self.current.val <= self.maximum:
            if self.current.val == self.maximum:
                self.flag = False
            return True
        else:
            return False

    # @return an integer, the next smallest number
    def next(self):
        res = self.current.val
        if self.flag:
            self.path.pop(-1)
            if self.current.right == None:
                self.current = self.path[-1]
            else:
                self.current = self.current.right
                while self.current:
                    self.path.append(self.current)
                    self.current = self.current.left
                self.current = self.path[-1]
        return res

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
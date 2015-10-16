# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.number = []
        self.inorder(root)
        self.curPos = 0
        self.length = len(self.number)
    
    def inorder(self,root):
        if root == None: return
        self.inorder(root.left)
        self.number.append(root.val)
        self.inorder(root.right)
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.curPos < self.length

    # @return an integer, the next smallest number
    def next(self):
        a = self.number[self.curPos]
        self.curPos += 1
        return a
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
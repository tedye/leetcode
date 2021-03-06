# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.path = [root]
        
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.path[0] != None

    # @return an integer, the next smallest number
    def next(self):
        while self.path:
            cur = self.path[-1]
            if cur:
                self.path.append(cur.left)
            else:
                self.path.pop(-1)
                if self.path:
                    cur = self.path.pop(-1)
                    self.path.append(cur.right)
                    return cur.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:
            return []
        
        temp = [root]
        result = []
        while temp:
            result = [[node.val for node in temp]] + result
            buf = []
            for node in temp:
                if node.left != None:
                    buf.append(node.left)
                if node.right!= None:
                    buf.append(node.right)
            temp = buf
        return result
            
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root == None:
            return []
            
        temp = []
        temp.append(root)
        result = []
        while temp:
            layer = []
            for node in temp:
                layer.append(node.val)
            result.append(layer)
            
            buf = []
            for node in temp:
                if node.left != None:
                    buf.append(node.left)
                if node.right != None:
                    buf.append(node.right)
            temp = buf
        
        return result
                
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        result = []
        if root == None:
            return result
            
        temp = [root]
        cnt = 1
        while temp:
            result.append(list([node.val for node in temp]))
            
            buf = []
            if cnt % 2:
                for node in temp[::-1]:
                    if node.right != None:
                        buf.append(node.right)
                    if node.left != None:
                        buf.append(node.left)
            else:
                for node in temp[::-1]:
                    if node.left != None:
                        buf.append(node.left)
                    if node.right != None:
                        buf.append(node.right)
            temp = buf
            cnt += 1
        return result
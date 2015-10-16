# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        height = [0]
        return self.isBalancedHelper(root,height)
        
    def isBalancedHelper(self, root, height):
        if root == None:
            height[0] = 0
            return True
        hl = [0]
        hr = [0]
        l = self.isBalancedHelper(root.left, hl)
        r = self.isBalancedHelper(root.right, hr)
        
        height[0] = max(hl[0],hr[0]) + 1
        
        if abs(hl[0]-hr[0]) > 1:
            return False
        else: return (l and r)
        
        
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None: return True
        return self.isSymHelper(root.left,root.right)
        
    def isSymHelper(self,left,right):
        if left == None: return right == None
        if right == None: return False
        
        if left.val != right.val: return False
        
        if not self.isSymHelper(left.left,right.right): return False
        if not self.isSymHelper(left.right,right.left): return False
        
        return True
                    
                
                    

        
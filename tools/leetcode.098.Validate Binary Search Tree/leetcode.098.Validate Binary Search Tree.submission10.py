# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        # attempt one recursive
        if not root: return True
        val = []
        self.travesal(root,val)
        if len(val) ==1 :
            return True
        pos = 1
        length = len(val)
        while pos < length:
            if val[pos-1] < val[pos]:
                pos += 1
            else:
                return False
        return True
        
        
    def travesal(self, node, val):
        if not node:
            return
        
        self.travesal(node.left,val)
        val.append(node.val)
        self.travesal(node.right,val)
        
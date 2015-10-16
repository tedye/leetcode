# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        if not root: return 0
        if not root.right and not root.left: return root.val
        res = [0]
        s = [0]
        self.dfs(root,s,res)
        
        return res[0]
        
    def dfs(self,node,s,res):
        if not node: return
        if not node.right and not node.left:
            res[0] += 10 * s[0] + node.val
            return
        s[0] = 10 * s[0] + node.val
        self.dfs(node.left,s,res)
        self.dfs(node.right,s,res)
        s[0] -= node.val
        s[0] //= 10
        
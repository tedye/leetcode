# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        if not root: return []
        res = []
        cur = []
        self.helper(root,sum,res,cur)
        return res
    
    def helper(self,node,s,res,cur):
        if not node.right and not node.left:
            if s == node.val:
                cur.append(node.val)
                res.append(cur[:])
                cur.pop(-1)
            return
        cur.append(node.val)
        if node.left:
            self.helper(node.left, s - node.val,res,cur)
        if node.right:
            self.helper(node.right, s - node.val,res,cur)
        cur.pop(-1)
            
            
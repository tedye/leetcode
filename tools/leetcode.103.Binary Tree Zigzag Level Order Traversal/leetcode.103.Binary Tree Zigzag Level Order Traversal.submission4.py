# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if not root: return []
        
        lvl =[root]
        flag = True
        res = []
        while lvl:
            if flag:
                res.append([i.val for i in lvl])
            else:
                res.append([i.val for i in lvl][::-1])
            flag = not flag
            next_lvl = []
            for node in lvl:
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            lvl = next_lvl
        return res
        
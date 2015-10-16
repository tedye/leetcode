# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, s):
        if not root: return []
        
        res = []
        cur = []
        self.dfs(root,s,res,cur)
        return res

    def dfs(self,root,s,res,cur):
        if root.right == None and root.left == None:
            cur.append(root.val)
            if sum(cur) == s:
                res.append(cur[:]) 
            del cur[-1]
            return 

        if root.left != None:
            cur.append(root.val)
            self.dfs(root.left,s,res,cur)
            del cur[-1]
        if root.right != None:
            cur.append(root.val)
            self.dfs(root.right,s,res,cur)
            del cur[-1]

        
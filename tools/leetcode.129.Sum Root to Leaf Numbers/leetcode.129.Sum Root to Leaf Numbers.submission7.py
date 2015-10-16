# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root == None: return 0
        if root.right == root.left == None: return root.val
        
        num = [root.val]
        res = []
        self.dfs(root,num,res)
        return sum(res)
        
    def dfs(self,root,num,res):

        if root.left == root.right == None:
            res.append(self.getSum(num))
            del num[-1]
            return
        
        if root.left != None:
            num.append(root.left.val)
            self.dfs(root.left, num, res)
        if root.right != None:
            num.append(root.right.val)
            self.dfs(root.right, num, res)
        del num[-1]
            
    def getSum(self,num):
        if not num: return 0
        
        s = 0
        for i in num:
            s *= 10
            s += i
        return s

                
        
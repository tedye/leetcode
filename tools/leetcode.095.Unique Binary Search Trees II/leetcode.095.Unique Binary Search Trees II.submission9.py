# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        l = [i for i in range(1,n+1)]
        return self.helper(l)

    def helper(self,l):
        if not l: return [None]
        res = []
        for i in range(len(l)):
            l1 = l[:i]
            l2 = l[i+1:]
            res1 = self.helper(l1)
            res2 = self.helper(l2)
            for r1 in res1:
                for r2 in res2:
                    t = TreeNode(l[i])
                    t.left = r1
                    t.right = r2
                    res.append(t)
        return res
        
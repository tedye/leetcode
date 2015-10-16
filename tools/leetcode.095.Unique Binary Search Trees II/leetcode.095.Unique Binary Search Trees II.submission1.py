# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        return self.helper([i+1 for i in range(n)])
        
    def helper(self,n):
        if not n:
            return [None]
        res = []
        for i in range(len(n)):
            ltrees = self.helper(n[:i])
            rtrees = self.helper(n[i+1:])
            for l in ltrees:
                for r in rtrees:
                    res.append(TreeNode(n[i]))
                    res[-1].left = l
                    res[-1].right = r
        return res
        
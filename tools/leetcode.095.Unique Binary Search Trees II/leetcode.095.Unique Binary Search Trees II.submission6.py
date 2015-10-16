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
        
    def helper(self, nums):
        if not nums:
            return [None]
        res = []
        for i in range(len(nums)):
            left = self.helper(nums[:i])
            right = self.helper(nums[i+1:])
            for l in left:
                for r in right:
                    res.append(TreeNode(nums[i]))
                    res[-1].left = l
                    res[-1].right = r
        return res
        
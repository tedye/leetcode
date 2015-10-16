# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if not nums: return []
        
        nodes = [TreeNode(n) for n in nums]
        l = len(nums)
        cnt = 0
        temp = l
        while temp:
            cnt+=1
            temp //= 2
        padding = 2 ** cnt - 1 - l
        if padding > 0:
            x = []
            for i in nodes[-padding:]:
                x.append(i)
                x.append(None)
            nodes = nodes[:-padding] + x
        
        while len(nodes) > 1:
            nextlvl = []
            l = len(nodes)
            for i in range(l):
                if i & 1:
                    nodes[i].left = nodes[i-1]
                    if i+1 < l:
                        nodes[i].right = nodes[i+1]
                    nextlvl.append(nodes[i])
            nodes = nextlvl
        return nodes[0]
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self,root):
        if not root: 
            return 0
        depth = 0
        temp = root
        while temp.left:
            temp = temp.left
            depth += 1
        start = 0
        end = 2 ** depth-1
        res = end
        while start  < end:
            mid = start + (end-start) // 2
            a = self.exist(mid,root,depth)
            b = self.exist(mid+1,root,depth)
            if a and not b:
                start = mid
                break
            elif not a:
                end = mid -1
            elif a and b:
                start = mid + 1
        return start + res + 1
    
    def exist(self, n, node, depth):
        while depth > 0:
            if (n >> (depth-1)) & 1:
                node = node.right
            else:
                node = node.left
            depth -= 1
        return node != None
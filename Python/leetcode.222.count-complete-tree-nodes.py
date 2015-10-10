# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        depth = 0
        temp = root
        while temp.left:
            temp = temp.left
            depth += 1
        res = 2 ** depth - 1
        
        start = 0
        end = res
        while start < end:
            mid = start + (end-start) // 2
            a = self.exist(root,mid,depth)
            b = self.exist(root,mid+1,depth)
            if a and b:
                start = mid + 1
            elif not a:
                end = mid - 1
            elif a and not b:
                start = mid
                break
        return res +  start + 1
        
    def exist(self, node, m,depth):
        while depth > 0:
            if (m >> (depth - 1)) & 1 :
                node = node.right
            else:
                node = node.left
            depth -= 1
        return node != None
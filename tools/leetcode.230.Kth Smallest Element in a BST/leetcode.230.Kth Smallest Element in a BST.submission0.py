# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        i = 0
        path = [root]
        while i < k or path:
            cur = path[-1]
            if cur: 
                path.append(cur.left)
            else:
                path.pop(-1)
                if path:
                    i += 1
                    cur = path.pop(-1)
                    if i == k:
                        return cur.val
                    path.append(cur.right)
                
        return None
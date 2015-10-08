# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        if not root.right and not root.left: return [root.val]
        
        path = [root]
        res = []
        while path:
            cur = path[-1]
            if cur:
                res = [cur.val] + res
                path.append(cur.right)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    path.append(cur.left)
        return res
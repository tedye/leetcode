# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        path = [root]
        t = []
        while path:
            cur = path[-1]
            
            if cur:
                t.append(cur)
                path.append(cur.left)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    path.append(cur.right)
                    
        for i in range(len(t)-1):
            t[i].right = t[i+1]
            t[i].left = None
        t[-1].left = None
        t[-1].right = None
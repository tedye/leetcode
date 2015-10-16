# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
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
        
            
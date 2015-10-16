# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        if not root or not root.left and not root.right: return
    
        # inorder travesal from left
        l = [None, -0x7fffffff]
        path = [root]
        toexchangel = None
        while path:
            cur = path[-1]
            if cur:
                path.append(cur.left)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    if cur:
                        if l[1] > cur.val:
                            toexchangel = l[0]
                            break
                        else:
                            l = [cur,cur.val]
                    path.append(cur.right)
        # inorder travesal from right
        r = [None, 0x7fffffff]
        path = [root]
        toexchanger = None
        while path:
            cur = path[-1]
            if cur:
                path.append(cur.right)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    if cur:
                        if r[1] < cur.val:
                            toexchanger = r[0]
                            break
                        else:
                            r = [cur,cur.val]
                    path.append(cur.left)
        if toexchangel:
            temp = toexchangel.val
            toexchangel.val = toexchanger.val
            toexchanger.val = temp
        return 
        
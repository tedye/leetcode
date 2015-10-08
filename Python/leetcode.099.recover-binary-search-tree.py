# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        targetOne = None
        last = TreeNode(-0x7fffffff)
        
        path = [root]
        while path:
            cur = path[-1]
            if cur:
                path.append(cur.left)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    if cur.val < last.val:
                        targetOne = last
                        break
                    else:
                        last = cur
                    path.append(cur.right)
        path = [root]
        last = TreeNode(0x7fffffff)
        targetTwo = None
        while path:
            cur = path[-1]
            if cur:
                path.append(cur.right)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    if cur.val > last.val:
                        targetTwo = last
                        break
                    else:
                        last = cur
                    path.append(cur.left)
        temp = targetTwo.val
        targetTwo.val = targetOne.val
        targetOne.val = temp
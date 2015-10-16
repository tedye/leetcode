# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None: return
    
        queue = []
        queue.append(root)
        while queue:
            nextLevel = []
            for i in range(len(queue)-1):
                queue[i].next =queue[i+1]
                if queue[i].left != None: nextLevel.append(queue[i].left)
                if queue[i].right != None: nextLevel.append(queue[i].right)
            queue[-1].next = None
            if queue[-1].left != None: nextLevel.append(queue[-1].left)
            if queue[-1].right != None: nextLevel.append(queue[-1].right)
            queue = nextLevel
            
            
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
            for i in range(len(queue)-1):
                queue[i].next =queue[i+1]
            queue[-1].next = None
            
            nextLevel = []
            for node in queue:
                if node.left != None: nextLevel.append(node.left)
                if node.right != None: nextLevel.append(node.right)
            
            queue = nextLevel
            
            
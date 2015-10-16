# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        length = len(num)
        if length == 0: return None
        if length == 1: return TreeNode(num[0])
    
        cnt = 0
        temp = length
        while temp:
            cnt+=1
            temp //= 2
        padcnt = 2**cnt-1-length
        num = [TreeNode(n) for n in num]
        
        if padcnt > 0:
            newNum = num[:length-padcnt]
            for n in num[-padcnt:]:
                newNum.extend([n,None])
        else: newNum = num
        
        while len(newNum) != 1:
            temp = []
            for i in range(len(newNum)):
                if i % 2 == 1:
                    newNum[i].left = newNum[i-1]
                    newNum[i].right = newNum[i+1]
                    temp.append(newNum[i])
            newNum = temp
        return newNum[0]
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # 1. use Inorder travesal + heapq
        '''
        heap = []
        path = [root]
        while path:
            cur = path[-1]
            if cur:
                path.append(cur.left)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    # push the heap with absolute distance to target as comparing key
                    heapq.heappush(heap,(abs(cur.val * 1.0 - target), cur.val))
                    path.append(cur.right)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        # passed with around 120ms
        '''
        
        
        # 2. use inorder travesal + binary search + linear search
        # passed with 76 ms
        
        # get sorted array by inorder travesal
        inorder = []
        path = [root]
        while path:
            cur = path[-1]
            if cur:
                path.append(cur.left)
            else:
                path.pop(-1)
                if path:
                    cur = path.pop(-1)
                    inorder.append(cur.val)
                    path.append(cur.right)
        # do binary search to find the right position if we want to insert target
        left = 0
        right = len(inorder)
        result = []
        while left < right:
            mid = (right+left) // 2
            if inorder[mid] > target:
                right = mid
            else:
                left = mid + 1
                
        # search the both side for k nearest element
        if left == 0:
            return inorder[:k]
        if left == len(inorder):
            return inorder[-k:]
        if inorder[left] == target:
            result += inorder[mid],
            self.helper(inorder,mid-1,mid+1, result,target, k-1)
            return result
        self.helper(inorder,left-1,left, result,target, k)
        return result
        
    def helper(self,inorder,gol,gor,result,target,k):
        n = len(inorder)
        while k > 0:
            if gol >= 0 and gor < n:
                if abs(target - inorder[gol]) > abs(target - inorder[gor]):
                    result += inorder[gor],
                    gor += 1
                else:
                    result += inorder[gol],
                    gol -= 1
            elif gol >= 0:
                result += inorder[gol],
                gol -= 1
            elif gor < n:
                result += inorder[gor],
                gor += 1
            k -= 1
        
        
        
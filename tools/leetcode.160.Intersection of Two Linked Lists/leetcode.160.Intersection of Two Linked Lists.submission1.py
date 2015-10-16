# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        l1 = self.getLength(headA)
        l2 = self.getLength(headB)
        if l1 == 0 or l2 == 0:
            return None
        
        if l1 > l2:
            temp = headB
            headB = headA
            headA = temp
        advance = abs(l1-l2)
        
        i = 0
        while i < advance:
            headB = headB.next
            i += 1
        
        while headA and headB:
            if headA.val == headB.val:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
        
    def getLength(self,node):
        res = 0
        while node:
            node = node.next
            res += 1
        return res
            
        
            
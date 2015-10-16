# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB: return None
        
        flagA = True
        flagB = True
        tempA = headA
        tempB = headB
        while tempA and tempB:
            if tempA.val == tempB.val: 
                return tempA
            tempA = tempA.next
            if not tempA and flagA:
                tempA = headB
                flagA = False
            tempB = tempB.next
            if not tempB and flagB:
                tempB = headA
                flagB = False
        return None
        
            
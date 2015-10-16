# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None: return None
        
        tempA = headA
        A = True
        tempB = headB
        B = True
        while tempA != None and tempB != None:
            if tempA == tempB: return tempA
            tempA = tempA.next
            tempB = tempB.next
            if tempA == None and A:
                tempA = headB
                A = False
            if tempB ==None and B:
                tempB = headA
                B = False
        return None

            
                
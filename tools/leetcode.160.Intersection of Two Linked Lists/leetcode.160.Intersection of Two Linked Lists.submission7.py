# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        tempa = headA
        tempb = headB
        flaga = False
        flagb = False
        while tempa != tempb:
            if tempa == None:
                if not flaga:
                    flag = True
                    tempa = headB
                else:
                    return None
            else:
                tempa = tempa.next
            if tempb == None:
                if not flagb:
                    flagb = True
                    tempb = headA
                else: 
                    return None
            else:
                tempb = tempb.next
        return tempa
        
        
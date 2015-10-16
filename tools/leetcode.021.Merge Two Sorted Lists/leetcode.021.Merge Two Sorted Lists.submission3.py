# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        
        temp1 = l1
        temp2 = l2
        temp3 = ListNode(-1) # dummy head
        temp = temp3
        while temp1 != None and temp2 != None:
            if temp1.val <= temp2.val:
                temp3.next = temp1
                temp1 = temp1.next
                temp3 = temp3.next
            elif temp1.val > temp2.val:
                temp3.next = temp2
                temp2 = temp2.next
                temp3 = temp3.next
                
        if temp1 == None:
            temp3.next = temp2
        elif temp2 == None:
            temp3.next = temp1
        
        return temp.next